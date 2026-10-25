#!/usr/bin/env python3
"""通用质检脚本：编译 / 样例 / 随机对拍 / 计时。

用法:
    python shared/check.py problems/<分类>/<slug> [--stress N] [--no-cpp]
    python shared/check.py --all [--stress N]

约定（见 docs/guide.md）:
    <slug>/cpp/solution.cpp        C++ 主解（自带 main，stdin/stdout）
    <slug>/python/solution.py      Python 主解（自带 main，stdin/stdout）
    <slug>/tests/samples/*.in|out  样例
    <slug>/tests/gen.py            随机生成器：python gen.py [seed] -> 打印输入
    <slug>/tests/brute.py          暴力参考解：stdin -> stdout
"""
import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------- 工具


def find_gxx(arg=None):
    if arg:
        return arg
    env = os.environ.get("GXX")
    if env:
        return env
    for name in ("g++", "clang++"):
        p = shutil.which(name)
        if p:
            return p
    # WinLibs (winget) / MSYS2 常见位置的兜底
    candidates = [
        Path(r"C:\Users\admin\AppData\Local\Microsoft\WinGet\Packages"),
        Path(r"C:\Program Files\WinLibs"),
        Path(r"C:\msys64\ucrt64\bin"),
        Path(r"D:\msys64\ucrt64\bin"),
        Path(r"D:\msys64\mingw64\bin"),
    ]
    for base in candidates:
        if base.exists():
            for p in base.glob("**/bin/g++.exe"):
                return str(p)
    return None


def norm(text):
    """统一输出：去行尾空白，去末尾空行。"""
    lines = [ln.rstrip() for ln in text.replace("\r\n", "\n").split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def compare(prob_dir, data, expected, got, checker):
    """比较输出；有多解题目由 tests/checker.py 判定语义。

    checker 接口：python checker.py <input> <expected> <got>，
    退出码 0 表示通过，否则 stdout/stderr 给出原因。
    """
    if checker is None:
        ok = got == expected
        msg = f"expected:\n{expected[:800]}\n---\ngot:\n{got[:800]}"
        return ok, msg
    tmp = Path(prob_dir) / "tests" / "tmp"
    tmp.mkdir(exist_ok=True)
    inp = tmp / "cmp.in"
    exp = tmp / "cmp.expected"
    g = tmp / "cmp.got"
    inp.write_bytes(data if isinstance(data, bytes) else data.encode())
    exp.write_text(expected, encoding="utf-8")
    g.write_text(got, encoding="utf-8")
    r = run([sys.executable, str(checker), str(inp), str(exp), str(g)], timeout=60)
    msg = (r.stdout + r.stderr).decode("utf-8", "replace")[:800]
    return r.returncode == 0, msg


def run(cmd, data=b"", timeout=60):
    return subprocess.run(cmd, input=data, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, timeout=timeout)


# ---------------------------------------------------------------- 单题检查


def check_problem(prob_dir, stress, gxx, timeout, keep_cases=False):
    prob_dir = Path(prob_dir)
    name = prob_dir.name
    cpp_src = prob_dir / "cpp" / "solution.cpp"
    py_src = prob_dir / "python" / "solution.py"
    tests = prob_dir / "tests"
    samples = sorted(tests.glob("samples/*.in"))
    gen = tests / "gen.py"
    brute = tests / "brute.py"
    checker = tests / "checker.py"
    checker = checker if checker.exists() else None

    failures = []
    notes = []

    if not py_src.exists() and not cpp_src.exists():
        return [f"{name}: 找不到 cpp/solution.cpp 或 python/solution.py"], notes

    cpp_bin = None
    if cpp_src.exists():
        if gxx:
            build = prob_dir / "build"
            build.mkdir(exist_ok=True)
            cpp_bin = build / ("solution.exe" if os.name == "nt" else "solution")
            r = run([gxx, "-O2", "-std=c++17", "-o", str(cpp_bin), str(cpp_src)], timeout=120)
            if r.returncode != 0:
                failures.append(f"{name}: C++ 编译失败\n{r.stderr.decode('utf-8', 'replace')[:2000]}")
                cpp_bin = None
            else:
                notes.append(f"{name}: C++ 编译通过 ({gxx})")
        else:
            notes.append(f"{name}: 未找到 C++ 编译器，跳过 C++ 检查（可设 GXX）")

    runners = []
    if py_src.exists():
        runners.append(("python", [sys.executable, str(py_src)]))
    if cpp_bin:
        runners.append(("cpp", [str(cpp_bin)]))

    # 1) 样例
    for sample in samples:
        data = sample.read_bytes()
        out_file = sample.with_suffix(".out")
        if not out_file.exists():
            continue
        expected = norm(out_file.read_text(encoding="utf-8", errors="replace"))
        for label, cmd in runners:
            try:
                r = run(cmd, data, timeout=timeout)
            except subprocess.TimeoutExpired:
                failures.append(f"{name}/{sample.name} [{label}]: 超时")
                continue
            if r.returncode != 0:
                failures.append(f"{name}/{sample.name} [{label}]: 退出码 {r.returncode}\n"
                                f"{r.stderr.decode('utf-8', 'replace')[:800]}")
                continue
            got = norm(r.stdout.decode("utf-8", "replace"))
            ok, why = compare(prob_dir, data, expected, got, checker)
            if not ok:
                failures.append(f"{name}/{sample.name} [{label}]: 输出不一致\n{why}")

    # 2) 随机对拍（与暴力参考解）
    if stress > 0 and gen.exists() and brute.exists():
        tmp = tests / "tmp"
        tmp.mkdir(exist_ok=True)
        start = time.time()
        for i in range(stress):
            seed = str(i + 1)
            try:
                g = run([sys.executable, str(gen), seed], timeout=timeout)
            except subprocess.TimeoutExpired:
                failures.append(f"{name}: gen.py seed={seed} 超时")
                break
            if g.returncode != 0:
                failures.append(f"{name}: gen.py seed={seed} 失败:\n"
                                f"{g.stderr.decode('utf-8', 'replace')[:500]}")
                break
            data = g.stdout
            try:
                b = run([sys.executable, str(brute)], data, timeout=timeout * 2)
            except subprocess.TimeoutExpired:
                failures.append(f"{name}: brute.py seed={seed} 超时")
                break
            if b.returncode != 0:
                failures.append(f"{name}: brute.py seed={seed} 失败:\n"
                                f"{b.stderr.decode('utf-8', 'replace')[:500]}")
                break
            expected = norm(b.stdout.decode("utf-8", "replace"))
            for label, cmd in runners:
                try:
                    r = run(cmd, data, timeout=timeout)
                except subprocess.TimeoutExpired:
                    failures.append(f"{name}: {label} seed={seed} 超时")
                    continue
                got = norm(r.stdout.decode("utf-8", "replace"))
                ok, why = compare(prob_dir, data, expected, got, checker)
                if r.returncode != 0 or not ok:
                    if keep_cases:
                        (tmp / f"fail_seed{seed}.in").write_bytes(data)
                        (tmp / f"fail_seed{seed}.out").write_text(expected, encoding="utf-8")
                        (tmp / f"fail_seed{seed}.{label}.out").write_text(got, encoding="utf-8")
                    failures.append(f"{name}: 随机对拍失败 seed={seed} [{label}]\n{why}")
        if failures:
            pass  # 失败已在循环内记录
        else:
            notes.append(f"{name}: 随机对拍 {stress} 组通过 ({time.time() - start:.1f}s)")
    elif stress > 0:
        notes.append(f"{name}: 缺少 gen.py / brute.py，跳过随机对拍")

    return failures, notes


# ---------------------------------------------------------------- 主流程


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("target", nargs="?", help="题目目录")
    ap.add_argument("--all", action="store_true", help="检查 problems/ 下全部题目")
    ap.add_argument("--stress", type=int, default=200)
    ap.add_argument("--no-cpp", action="store_true")
    ap.add_argument("--gxx", default=None)
    ap.add_argument("--timeout", type=float, default=30)
    ap.add_argument("--keep-cases", action="store_true")
    args = ap.parse_args(argv)

    gxx = None if args.no_cpp else find_gxx(args.gxx)
    targets = []
    if args.all:
        targets = sorted(p.parent.parent for p in (ROOT / "problems").glob("*/*/cpp/solution.cpp"))
        targets += sorted(p.parent.parent for p in (ROOT / "problems").glob("*/*/python/solution.py"))
        targets = sorted(set(targets))
    elif args.target:
        targets = [Path(args.target)]
    else:
        ap.print_help()
        return 2

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    all_failures = []
    for t in targets:
        if not t.is_absolute():
            t = (ROOT / t) if (ROOT / t).exists() else Path(t)
        failures, notes = check_problem(t, args.stress, gxx, args.timeout, args.keep_cases)
        for n in notes:
            print("·", n)
        all_failures.extend(failures)

    if all_failures:
        print("\n[FAIL] %d 项：" % len(all_failures))
        for f in all_failures:
            print("-", f)
        return 1
    print("\n[PASS] 全部通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
