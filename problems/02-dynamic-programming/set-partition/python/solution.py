"""2-7 集合划分（Bell 数，Python 版，Stirling 滚动 DP）。"""

import sys


def bell(n: int) -> int:
    S = [0] * (n + 1)
    S[0] = 1
    for i in range(1, n + 1):
        for k in range(i, 0, -1):
            S[k] = S[k - 1] + k * S[k]
        S[0] = 0
    return sum(S)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    print(bell(n))


if __name__ == "__main__":
    main()
