"""3-4 数字三角形（Python 版，自底向上）。"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    a, p = [], 1
    for i in range(n):
        a.append(list(map(int, data[p:p + i + 1])))
        p += i + 1
    dp = [row[:] for row in a]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] = a[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1])

    path = []
    j = 0
    for i in range(n):
        path.append(a[i][j])
        if i + 1 < n and dp[i + 1][j + 1] > dp[i + 1][j]:
            j += 1
    sys.stdout.write(str(dp[0][0]) + "\n" + " ".join(map(str, path)) + "\n")


if __name__ == "__main__":
    main()
