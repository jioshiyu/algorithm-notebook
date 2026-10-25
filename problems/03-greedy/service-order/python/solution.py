"""4-7 多处最优服务次序（Python 版，贪心 + 小根堆）。"""

import heapq
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, s = int(data[0]), int(data[1])
    t = list(map(int, data[2:2 + n]))
    order = sorted(range(n), key=lambda i: (t[i], i))

    pq = [(0, r) for r in range(1, s + 1)]
    heapq.heapify(pq)
    srv = [0] * n
    start = [0] * n
    sum_start = 0
    for idx in order:
        free_at, r = heapq.heappop(pq)
        srv[idx] = r
        start[idx] = free_at
        sum_start += free_at
        heapq.heappush(pq, (free_at + t[idx], r))

    out = [f"{sum_start / n:.2f}"]
    for i in range(n):
        out.append(f"{i + 1} {srv[i]} {start[i]}")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
