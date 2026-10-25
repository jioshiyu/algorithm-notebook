"""1-1 统计数字问题（Python 版，与 cpp/solution.cpp 同算法）。"""

import sys


def count_digit(n: int, d: int) -> int:
    """1..n 的十进制写法中数字 d 出现的次数（无前导零）。"""
    cnt = 0
    base = 1
    while base <= n:
        high = n // (base * 10)
        cur = (n // base) % 10
        low = n % base
        if d != 0:
            if cur > d:
                cnt += (high + 1) * base
            elif cur == d:
                cnt += high * base + low + 1
            else:
                cnt += high * base
        elif high > 0:  # d == 0：去掉前导零
            cnt += high * base if cur > 0 else (high - 1) * base + low + 1
        base *= 10
    return cnt


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    out = [str(count_digit(n, d)) for d in range(10)]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
