"""5-4 运动员最佳配对（Python 版，状压 DP）。"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    vals = list(map(int, data[1:]))
    P = [vals[i * n:(i + 1) * n] for i in range(n)]
    off = n * n
    Q = [vals[off + i * n:off + (i + 1) * n] for i in range(n)]

    full = 1 << n
    NEG = None
    dp = [NEG] * full
    pre = [-1] * full
    pc = [0] * full
    for mask in range(1, full):
        pc[mask] = pc[mask >> 1] + (mask & 1)
    dp[0] = 0
    for mask in range(full):
        if dp[mask] is None:
            continue
        i = pc[mask]
        if i == n:
            continue
        for j in range(n):
            if mask & (1 << j):
                continue
            nm = mask | (1 << j)
            cand = dp[mask] + P[i][j] * Q[j][i]
            if dp[nm] is None or cand > dp[nm]:
                dp[nm] = cand
                pre[nm] = j

    mask = full - 1
    match = [0] * n
    for i in range(n - 1, -1, -1):
        j = pre[mask]
        match[i] = j + 1
        mask ^= (1 << j)
    sys.stdout.write(str(dp[full - 1]) + "\n" + " ".join(map(str, match)) + "\n")


if __name__ == "__main__":
    main()
