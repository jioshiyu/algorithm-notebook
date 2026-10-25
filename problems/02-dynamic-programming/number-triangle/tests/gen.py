"""随机用例：python gen.py [seed] -> n 与三角形（含负数）。"""

import random
import sys


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    n = rng.choice([1, 2, 3, 4, 5, 6, 8, 10, 12])
    print(n)
    for i in range(n):
        print(" ".join(str(rng.randint(-9, 9)) for _ in range(i + 1)))


if __name__ == "__main__":
    main()
