"""随机用例：python gen.py [seed] -> 打印 n（1..15，兼顾对拍速度）。"""

import random
import sys


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    n = rng.choice([1, 1, 2, 3, 4, 5, 6, 8, 10, 12, 15])
    print(n)


if __name__ == "__main__":
    main()
