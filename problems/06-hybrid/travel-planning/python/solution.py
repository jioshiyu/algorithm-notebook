"""大作业 旅行规划（Python 版，折半搜索）。"""

import sys
from collections import defaultdict


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, target = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))

    h = n // 2

    def enum(lo: int, hi: int):
        out = []
        for mask in range(1 << (hi - lo)):
            s = 0
            for b in range(hi - lo):
                if mask >> b & 1:
                    s += a[lo + b]
            out.append((s, mask))
        return out

    left = enum(0, h)
    right = enum(h, n)
    by_sum = defaultdict(list)
    for s, mask in right:
        by_sum[s].append(mask)

    combos = []
    for ls, lmask in left:
        need = target - ls
        for rmask in by_sum.get(need, []):
            ids = [b + 1 for b in range(h) if lmask >> b & 1]
            ids += [h + b + 1 for b in range(n - h) if rmask >> b & 1]
            ids.sort()
            combos.append(tuple(ids))
    combos = sorted(set(combos))
    sys.stdout.write(str(len(combos)) + "\n")
    for ids in combos:
        sys.stdout.write(" ".join(map(str, ids)) + "\n")


if __name__ == "__main__":
    main()
