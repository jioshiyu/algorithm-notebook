"""暴力参考解：O(n^2) DP，输出长度 + 一条 LIS。"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    if n == 0:
        print(0)
        print()
        return
    dp = [1] * n
    pre = [-1] * n
    best, last = 0, 0
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                pre[i] = j
        if dp[i] > best:
            best, last = dp[i], i
    path = []
    cur = last
    while cur != -1:
        path.append(a[cur])
        cur = pre[cur]
    path.reverse()
    print(len(path))
    print(" ".join(map(str, path)))


if __name__ == "__main__":
    main()
