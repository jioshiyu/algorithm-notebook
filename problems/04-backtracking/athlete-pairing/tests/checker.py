"""配对 checker：最大值一致 + 配对是排列 + 总值自洽。"""

import sys


def main() -> None:
    inp = open(sys.argv[1], "rb").read().split()
    n = int(inp[0])
    vals = list(map(int, inp[1:]))
    P = [vals[i * n:(i + 1) * n] for i in range(n)]
    off = n * n
    Q = [vals[off + i * n:off + (i + 1) * n] for i in range(n)]

    exp = open(sys.argv[2], encoding="utf-8").read().strip().split("\n")
    got = [ln for ln in open(sys.argv[3], encoding="utf-8").read().split("\n") if ln.strip()]
    exp_val = int(exp[0])
    if int(got[0]) != exp_val:
        print(f"最优值错误: got {got[0]}, expected {exp_val}")
        raise SystemExit(1)
    perm = list(map(int, got[1].split())) if len(got) > 1 else []
    if sorted(perm) != list(range(1, n + 1)):
        print(f"不是 1..{n} 的排列: {perm}")
        raise SystemExit(1)
    total = sum(P[i][perm[i] - 1] * Q[perm[i] - 1][i] for i in range(n))
    if total != exp_val:
        print(f"配对总值 {total} != 输出值 {exp_val}")
        raise SystemExit(1)
    print("OK")


if __name__ == "__main__":
    main()
