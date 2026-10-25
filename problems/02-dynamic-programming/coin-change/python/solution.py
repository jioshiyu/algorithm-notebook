"""选做 3-0 硬币问题（Python 版，单调队列优化）。"""

import sys
from collections import deque


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    val = list(map(int, data[1:1 + n]))
    cnt = list(map(int, data[1 + n:1 + 2 * n]))
    m = int(data[1 + 2 * n])

    INF = 10**18
    dp = [INF] * (m + 1)
    dp[0] = 0
    used = [[0] * (m + 1) for _ in range(n)]

    for i in range(n):
        v, c = val[i], cnt[i]
        if c <= 0 or v > m:
            continue
        ndp = [INF] * (m + 1)
        for r in range(min(v, m + 1)):
            dq = deque()  # 存 x，保持 dp[r+x*v]-x 递增
            x = 0
            while r + x * v <= m:
                j = r + x * v
                if dp[j] != INF:
                    cur = dp[j] - x
                    while dq and dp[r + dq[-1] * v] - dq[-1] >= cur:
                        dq.pop()
                    dq.append(x)
                while dq and dq[0] < x - c:
                    dq.popleft()
                if dq:
                    bx = dq[0]
                    ndp[j] = dp[r + bx * v] + (x - bx)
                    used[i][j] = x - bx
                x += 1
        dp = ndp

    if dp[m] == INF:
        print("No solution")
        return
    j = m
    use = [0] * n
    for i in range(n - 1, -1, -1):
        k = used[i][j]
        use[i] = k
        j -= k * val[i]
    out = [str(dp[m])]
    for i in range(n):
        if use[i]:
            out.append(f"{val[i]} {use[i]}")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
