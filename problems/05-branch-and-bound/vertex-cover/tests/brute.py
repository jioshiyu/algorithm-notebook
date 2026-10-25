"""暴力参考解：枚举 2^n 个子集（n <= 12）。"""

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

    best = None
    best_mask = 0
    for mask in range(1 << n):
        ok = True
        for u, v in edges:
            if not (mask >> u) & 1 and not (mask >> v) & 1:
                ok = False
                break
        if not ok:
            continue
        cost = sum(w[i] for i in range(n) if (mask >> i) & 1)
        if best is None or cost < best:
            best, best_mask = cost, mask
    print(best)
    print(" ".join(str(i + 1) for i in range(n) if (best_mask >> i) & 1))


if __name__ == "__main__":
    main()
