"""暴力参考解：线性扫描最早空闲服务台（O(n^2)），输出同一格式。"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, s = int(data[0]), int(data[1])
    t = list(map(int, data[2:2 + n]))
    order = sorted(range(n), key=lambda i: (t[i], i))

    free_at = [0] * (s + 1)
    srv = [0] * n
    start = [0] * n
    sum_start = 0
    for idx in order:
        pick = 1
        for r in range(2, s + 1):
            if free_at[r] < free_at[pick]:
                pick = r
        srv[idx] = pick
        start[idx] = free_at[pick]
        sum_start += free_at[pick]
        free_at[pick] += t[idx]

    print(f"{sum_start / n:.2f}")
    for i in range(n):
        print(i + 1, srv[i], start[i])


if __name__ == "__main__":
    main()
