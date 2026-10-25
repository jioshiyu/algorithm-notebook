"""选做 2-1 众数（Python 版）。"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    a = sorted(map(int, data[1:1 + n]))
    if not a:
        print(0)
        print(0)
        return
    best_val, best_cnt = a[0], 1
    cur_val, cur_cnt = a[0], 1
    for x in a[1:]:
        if x == cur_val:
            cur_cnt += 1
        else:
            cur_val, cur_cnt = x, 1
        if cur_cnt > best_cnt:
            best_val, best_cnt = cur_val, cur_cnt
    print(best_val)
    print(best_cnt)


if __name__ == "__main__":
    main()
