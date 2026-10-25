"""随机用例：python gen.py [seed] -> n 与 n 个元素（含重复）。"""

import random
import sys


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    n = rng.randint(1, 300)
    vals = [rng.randint(-30, 30) for _ in range(n)]
    print(n)
    print(" ".join(map(str, vals)))


if __name__ == "__main__":
    main()
