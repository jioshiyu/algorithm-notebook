"""3-1 LIS（Python 版，贪心 + 二分）。"""

import sys
from bisect import bisect_left


def solve(a: list[int]):
    n = len(a)
    tail: list[int] = []       # 长度 k+1 的最小结尾值
    tail_idx: list[int] = []   # 对应下标
    pre = [-1] * n
    for i, x in enumerate(a):
        pos = bisect_left(tail, x)
        if pos == len(tail):
            tail.append(x)
            tail_idx.append(i)
        else:
            tail[pos] = x
            tail_idx[pos] = i
        if pos > 0:
            pre[i] = tail_idx[pos - 1]
    path = []
    cur = tail_idx[-1]
    while cur != -1:
        path.append(a[cur])
        cur = pre[cur]
    path.reverse()
    return path


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    if not a:
        sys.stdout.write("0\n\n")
        return
    path = solve(a)
    sys.stdout.write(str(len(path)) + "\n" + " ".join(map(str, path)) + "\n")


if __name__ == "__main__":
    main()
