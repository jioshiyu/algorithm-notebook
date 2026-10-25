"""6-2 顶点覆盖（Python 版，分支限界，状态里带选择掩码）。"""

import heapq
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, m = int(data[0]), int(data[1])
    w = list(map(int, data[2:2 + n]))
    p = 2 + n
    edges = []
    for _ in range(m):
        edges.append((int(data[p]) - 1, int(data[p + 1]) - 1))
        p += 2

    inc = [0] * n
    for i, (u, v) in enumerate(edges):
        inc[u] |= 1 << i
        inc[v] |= 1 << i
    full = (1 << m) - 1

    def bound(cost: int, cov: int) -> int:
        # 极大匹配下界：互不相邻的未覆盖边各取 min 端点权；共享顶点的边不相加
        used = [False] * n
        s = cost
        for i, (u, v) in enumerate(edges):
            if (cov >> i) & 1:
                continue
            if used[u] or used[v]:
                continue
            used[u] = used[v] = True
            s += min(w[u], w[v])
        return s

    best = [10**18, 0]
    pq = [(0, 0, 0, 0, 0)]  # (bound, level, cost, covered, selected)
    while pq:
        lb, level, cost, cov, sel = heapq.heappop(pq)
        if lb >= best[0]:
            continue
        if level == n:
            if cov == full and cost < best[0]:
                best = [cost, sel]
            continue
        v = level
        heapq.heappush(pq, (bound(cost, cov), v + 1, cost, cov, sel))
        nc, ncov = cost + w[v], cov | inc[v]
        if nc < best[0]:
            heapq.heappush(pq, (bound(nc, ncov), v + 1, nc, ncov, sel | (1 << v)))

    sel_mask = best[1]
    chosen = [i + 1 for i in range(n) if (sel_mask >> i) & 1]
    print(best[0])
    print(" ".join(map(str, chosen)))


if __name__ == "__main__":
    main()
