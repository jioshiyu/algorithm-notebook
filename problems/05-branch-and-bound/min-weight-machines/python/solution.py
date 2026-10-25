"""5-3 最小重量机器设计（Python 版，分支限界）。"""

import heapq
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, m, d = int(data[0]), int(data[1]), int(data[2])
    vals = list(map(int, data[3:]))
    c = [vals[i * m:(i + 1) * m] for i in range(n)]
    w = [vals[n * m + i * m:n * m + (i + 1) * m] for i in range(n)]

    suffix = [0] * (n + 1)  # 每件都取最小重量时的剩余下界
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + min(w[i])

    best = [None, ()]  # (weight, path)
    pq = [(suffix[0], 0, 0, 0, ())]  # (bound, level, cost, weight, path)
    while pq:
        bound, level, cost, weight, path = heapq.heappop(pq)
        if best[0] is not None and weight + suffix[level] >= best[0]:
            continue
        if level == n:
            if cost <= d and (best[0] is None or weight < best[0]):
                best = [weight, path]
            continue
        for j in range(m):
            nc = cost + c[level][j]
            if nc > d:
                continue
            nw = weight + w[level][j]
            if best[0] is not None and nw + suffix[level + 1] >= best[0]:
                continue
            heapq.heappush(pq, (nw + suffix[level + 1], level + 1, nc, nw, path + (j + 1,)))

    if best[0] is None:
        print("No solution")
        return
    print(best[0])
    print(" ".join(map(str, best[1])))


if __name__ == "__main__":
    main()
