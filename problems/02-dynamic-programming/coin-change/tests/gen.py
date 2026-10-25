"""随机用例：python gen.py [seed] -> n、面值、数量、m。"""

import random
import sys


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    n = rng.randint(1, 5)
    vals = rng.sample(range(1, 12), n)
    vals.sort()
    counts = [rng.randint(0, 5) for _ in range(n)]
    m = rng.randint(0, 50)
    print(n)
    print(" ".join(map(str, vals)))
    print(" ".join(map(str, counts)))
    print(m)


if __name__ == "__main__":
    main()
