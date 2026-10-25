"""暴力参考解：枚举 m^n 种组合（小规模）。"""

import itertools
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, m, d = int(data[0]), int(data[1]), int(data[2])
    vals = list(map(int, data[3:]))
    c = [vals[i * m:(i + 1) * m] for i in range(n)]
    w = [vals[n * m + i * m:n * m + (i + 1) * m] for i in range(n)]

    best = None
    for pick in itertools.product(range(m), repeat=n):
        cost = sum(c[i][pick[i]] for i in range(n))
        if cost > d:
            continue
        weight = sum(w[i][pick[i]] for i in range(n))
        if best is None or weight < best[0]:
            best = (weight, pick)
    if best is None:
        print("No solution")
    else:
        print(best[0])
        print(" ".join(str(x + 1) for x in best[1]))


if __name__ == "__main__":
    main()
