"""随机用例：python gen.py [seed] -> n（0..25）。"""

import random
import sys


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    print(rng.randint(0, 25))


if __name__ == "__main__":
    main()
