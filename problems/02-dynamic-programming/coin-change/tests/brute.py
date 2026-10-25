"""暴力参考解：逐面值多重背包 DP（独立实现，m 较小）。"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    val = list(map(int, data[1:1 + n]))
    cnt = list(map(int, data[1 + n:1 + 2 * n]))
    m = int(data[1 + 2 * n])
    INF = 10**18
    dp = [[INF] * (m + 1) for _ in range(n + 1)]
    take = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(m + 1):
            if dp[i - 1][j] == INF:
                continue
            for k in range(cnt[i - 1] + 1):
                nj = j + k * val[i - 1]
                if nj > m:
                    break
                nc = dp[i - 1][j] + k
                if nc < dp[i][nj]:
                    dp[i][nj] = nc
                    take[i][nj] = k
    if dp[n][m] == INF:
        print("No solution")
        return
    used = [0] * n
    j = m
    for i in range(n, 0, -1):
        k = take[i][j]
        used[i - 1] = k
        j -= k * val[i - 1]
    print(dp[n][m])
    for i in range(n):
        if used[i]:
            print(val[i], used[i])


if __name__ == "__main__":
    main()
