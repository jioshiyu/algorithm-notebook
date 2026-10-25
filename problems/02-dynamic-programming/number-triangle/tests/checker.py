"""数字三角形 checker：和一致 + 路径是合法“走法”（每步同列或右一列）。

用法: python checker.py <input> <expected> <got>
"""

import sys


def main() -> None:
    inp = open(sys.argv[1], "rb").read().split()
    n = int(inp[0])
    a, p = [], 1
    for i in range(n):
        a.append(list(map(int, inp[p:p + i + 1])))
        p += i + 1

    exp = [ln for ln in open(sys.argv[2], encoding="utf-8").read().split("\n") if ln.strip()]
    got = [ln for ln in open(sys.argv[3], encoding="utf-8").read().split("\n") if ln.strip()]
    exp_sum = int(exp[0])
    got_sum = int(got[0])
    path = list(map(int, got[1].split())) if len(got) > 1 else []

    if got_sum != exp_sum:
        print(f"最大和错误: got {got_sum}, expected {exp_sum}")
        raise SystemExit(1)
    if len(path) != n:
        print(f"路径长度 {len(path)} != {n}")
        raise SystemExit(1)

    cols = {0}
    total = 0
    for i in range(n):
        matched = {c for c in cols if 0 <= c <= i and a[i][c] == path[i]}
        if not matched:
            print(f"第 {i} 行路径值 {path[i]} 无法从可行列 {sorted(cols)} 走出")
            raise SystemExit(1)
        cols = {x for c in matched for x in (c, c + 1) if x <= i + 1}
        total += path[i]
    if total != got_sum:
        print(f"路径和 {total} != 输出和 {got_sum}")
        raise SystemExit(1)
    print("OK")


if __name__ == "__main__":
    main()
