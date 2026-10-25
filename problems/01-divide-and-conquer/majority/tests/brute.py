"""暴力参考解：O(n^2) 统计，平手取数值最小者。"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    if not a:
        print(0)
        print(0)
        return
    best_val, best_cnt = min(a), 0
    for x in set(a):
        c = sum(1 for y in a if y == x)
        if c > best_cnt or (c == best_cnt and x < best_val):
            best_val, best_cnt = x, c
    print(best_val)
    print(best_cnt)


if __name__ == "__main__":
    main()
