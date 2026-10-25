"""暴力/独立参考解：利用 B(n)=Σ_{k=0}^{n-1} C(n-1,k)·B(k) 递推。"""

import math
import sys


def bell(n: int) -> int:
    B = [0] * (n + 1)
    B[0] = 1
    for i in range(1, n + 1):
        B[i] = sum(math.comb(i - 1, k) * B[k] for k in range(i))
    return B[n]


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    print(bell(n))


if __name__ == "__main__":
    main()
