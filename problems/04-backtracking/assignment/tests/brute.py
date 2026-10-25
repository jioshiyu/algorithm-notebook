"""暴力参考解：枚举全排列（n <= 8）。"""

import itertools
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    vals = list(map(int, data[1:1 + n * n]))
    c = [vals[i * n:(i + 1) * n] for i in range(n)]
    best = None
    best_p = None
    for perm in itertools.permutations(range(n)):
        s = sum(c[i][perm[i]] for i in range(n))
        if best is None or s < best:
            best, best_p = s, perm
    print(best)
    print(" ".join(str(j + 1) for j in best_p))


if __name__ == "__main__":
    main()
