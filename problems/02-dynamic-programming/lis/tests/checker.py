"""LIS 语义检查器：允许多条答案，校验长度与子序列合法性。

用法: python checker.py <input> <expected> <got>
"""

import sys


def read_seq(path):
    lines = open(path, encoding="utf-8", errors="replace").read().strip().split("\n")
    lines = [ln.strip() for ln in lines if ln.strip()]
    if not lines:
        return 0, []
    L = int(lines[0])
    seq = list(map(int, lines[1].split())) if len(lines) > 1 else []
    return L, seq


def main() -> None:
    inp = open(sys.argv[1], "rb").read().split()
    n = int(inp[0])
    a = list(map(int, inp[1:1 + n]))
    exp_len, _ = read_seq(sys.argv[2])
    got_len, got = read_seq(sys.argv[3])

    if got_len != exp_len:
        print(f"长度不符: got {got_len}, expected {exp_len}")
        raise SystemExit(1)
    if len(got) != got_len:
        print(f"序列元素个数 {len(got)} 与长度 {got_len} 不符")
        raise SystemExit(1)
    for x, y in zip(got, got[1:]):
        if not x < y:
            print(f"不是严格递增: {x} 后跟 {y}")
            raise SystemExit(1)
    # 子序列检查
    j = 0
    for x in a:
        if j < len(got) and x == got[j]:
            j += 1
    if j != len(got):
        print("输出不是输入的子序列")
        raise SystemExit(1)
    print("OK")


if __name__ == "__main__":
    main()
