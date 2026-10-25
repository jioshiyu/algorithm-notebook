"""随机用例生成器：python gen.py [seed] -> 打印一行 n。

覆盖：小规模随机、10 的幂附近边界、大规模随机（1e6~1e18）。
"""

import random
import sys


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    p = seed % 10
    if p <= 2:  # 10 的幂附近
        k = rng.randint(1, 18)
        n = 10**k + rng.choice([-1, 0, 1])
        n = max(1, min(n, 10**18))
    elif p <= 5:  # 小规模随机
        n = rng.randint(1, 100000)
    elif p <= 8:  # 中等规模
        n = rng.randint(1, 10**9)
    else:  # 大规模
        n = rng.randint(10**9, 10**18)
    print(n)


if __name__ == "__main__":
    main()
