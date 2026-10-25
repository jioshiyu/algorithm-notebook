"""工作分配 checker：最小费用一致 + 分配是排列 + 费用自洽。"""

import sys


def main() -> None:
    inp = open(sys.argv[1], "rb").read().split()
    n = int(inp[0])
    vals = list(map(int, inp[1:1 + n * n]))
    c = [vals[i * n:(i + 1) * n] for i in range(n)]

    exp = [ln for ln in open(sys.argv[2], encoding="utf-8").read().split("\n") if ln.strip()]
    got = [ln for ln in open(sys.argv[3], encoding="utf-8").read().split("\n") if ln.strip()]
    if not got:
        print("输出为空（程序可能崩溃）")
        raise SystemExit(1)
    if int(got[0]) != int(exp[0]):
        print(f"最小费用错误: got {got[0]}, expected {exp[0]}")
        raise SystemExit(1)
    perm = list(map(int, got[1].split())) if len(got) > 1 else []
    if sorted(perm) != list(range(1, n + 1)):
        print(f"不是 1..{n} 的排列: {perm}")
        raise SystemExit(1)
    total = sum(c[i][perm[i] - 1] for i in range(n))
    if total != int(exp[0]):
        print(f"费用和 {total} != 输出值 {exp[0]}")
        raise SystemExit(1)
    print("OK")


if __name__ == "__main__":
    main()
