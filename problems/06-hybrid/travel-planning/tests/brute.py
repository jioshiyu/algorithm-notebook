"""暴力参考解：枚举 2^n 个子集（n <= 18）。"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, target = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    combos = []
    for mask in range(1 << n):
        s = 0
        ids = []
        for b in range(n):
            if mask >> b & 1:
                s += a[b]
                ids.append(b + 1)
        if s == target:
            combos.append(tuple(ids))
    print(len(combos))
    for ids in combos:
        print(" ".join(map(str, ids)))


if __name__ == "__main__":
    main()
