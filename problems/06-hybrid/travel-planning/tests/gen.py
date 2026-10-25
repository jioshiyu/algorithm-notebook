"""随机用例：python gen.py [seed] -> n target 与票价（n <= 16，互不相同）。"""

import random
import sys


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    n = rng.randint(1, 16)
    prices = rng.sample(range(1, 40), n)
    target = rng.randint(1, sum(prices))
    print(n, target)
    print(" ".join(map(str, prices)))


if __name__ == "__main__":
    main()
