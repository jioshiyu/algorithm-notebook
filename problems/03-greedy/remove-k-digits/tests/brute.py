"""暴力参考解：枚举所有 C(n,k) 种删法取最小（n <= 12）。"""

import itertools
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    num = data[0].decode()
    k = int(data[1])
    n = len(num)
    if k >= n:
        print(0)
        return
    best = None
    for keep in itertools.combinations(range(n), n - k):
        s = "".join(num[i] for i in keep)
        v = int(s)
        if best is None or v < best:
            best = v
    print(best)


if __name__ == "__main__":
    main()
