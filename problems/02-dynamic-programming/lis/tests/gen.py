"""随机用例：python gen.py [seed] -> n 与数组（含重复值，考验严格递增）。"""

import random
import sys


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    n = rng.choice([0, 1, 2, 3, 5, 8, 12, 20, 50, 100, 150])
    vals = [rng.randint(-20, 20) for _ in range(n)]
    print(n)
    print(" ".join(map(str, vals)))


if __name__ == "__main__":
    main()
