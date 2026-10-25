"""最小机器 checker：最优重量一致 + 方案价格/重量自洽。"""

import sys


def main() -> None:
    inp = open(sys.argv[1], "rb").read().split()
    n, m, d = int(inp[0]), int(inp[1]), int(inp[2])
    vals = list(map(int, inp[3:]))
    c = [vals[i * m:(i + 1) * m] for i in range(n)]
    w = [vals[n * m + i * m:n * m + (i + 1) * m] for i in range(n)]

    # 独立 DP 求最优重量（价格维度）
    INF = float("inf")
    dp = [INF] * (d + 1)
    dp[0] = 0
    for i in range(n):
        ndp = [INF] * (d + 1)
        for j in range(d + 1):
            if dp[j] == INF:
                continue
            for k in range(m):
                nj = j + c[i][k]
                if nj <= d:
                    nw = dp[j] + w[i][k]
                    if nw < ndp[nj]:
                        ndp[nj] = nw
        dp = ndp
    best = min(dp)
    exp = "No solution" if best == INF else str(best)

    got = open(sys.argv[3], encoding="utf-8").read().strip().split("\n")
    if not got or not got[0].strip():
        print("输出为空")
        raise SystemExit(1)
    if exp == "No solution":
        if got[0].strip() != "No solution":
            print(f"应无解，got: {got[0]}")
            raise SystemExit(1)
        print("OK")
        return
    if got[0].strip() == "No solution":
        print(f"有解 {exp}，got No solution")
        raise SystemExit(1)
    got_w = int(got[0])
    pick = list(map(int, got[1].split())) if len(got) > 1 else []
    if got_w != int(exp):
        print(f"最优重量错误: got {got_w}, expected {exp}")
        raise SystemExit(1)
    if len(pick) != n or any(not (1 <= x <= m) for x in pick):
        print("方案编号非法")
        raise SystemExit(1)
    cost = sum(c[i][pick[i] - 1] for i in range(n))
    weight = sum(w[i][pick[i] - 1] for i in range(n))
    if cost > d or weight != got_w:
        print(f"方案自相矛盾: price={cost} (>d={d}?) weight={weight} vs {got_w}")
        raise SystemExit(1)
    print("OK")


if __name__ == "__main__":
    main()
