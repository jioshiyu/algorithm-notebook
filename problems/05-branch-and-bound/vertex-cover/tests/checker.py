"""顶点覆盖 checker：最优权值一致 + 覆盖合法 + 权值自洽。"""

import sys


def main() -> None:
    inp = open(sys.argv[1], "rb").read().split()
    n, m = int(inp[0]), int(inp[1])
    w = list(map(int, inp[2:2 + n]))
    p = 2 + n
    edges = []
    for _ in range(m):
        edges.append((int(inp[p]) - 1, int(inp[p + 1]) - 1))
        p += 2

    exp = open(sys.argv[2], encoding="utf-8").read().split("\n")
    exp_cost = int(exp[0])
    got = [ln for ln in open(sys.argv[3], encoding="utf-8").read().split("\n") if ln.strip()]
    if not got:
        print("输出为空（程序可能崩溃）")
        raise SystemExit(1)
    got_cost = int(got[0])
    sel = list(map(int, got[1].split())) if len(got) > 1 and got[1].strip() else []

    if got_cost != exp_cost:
        print(f"最优权值错误: got {got_cost}, expected {exp_cost}")
        raise SystemExit(1)
    chosen = set(x - 1 for x in sel)
    if any(not (0 <= x < n) for x in chosen):
        print("顶点编号越界")
        raise SystemExit(1)
    for u, v in edges:
        if u not in chosen and v not in chosen:
            print(f"边 ({u+1},{v+1}) 未被覆盖")
            raise SystemExit(1)
    total = sum(w[i] for i in chosen)
    if total != got_cost:
        print(f"权值和 {total} != 输出值 {got_cost}")
        raise SystemExit(1)
    print("OK")


if __name__ == "__main__":
    main()
