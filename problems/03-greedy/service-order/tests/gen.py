"""随机用例：python gen.py [seed] -> n, s, 服务时间。"""

import random
import sys


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    n = rng.randint(1, 150)
    s = rng.randint(1, min(n, 6))
    times = [rng.randint(1, 30) for _ in range(n)]
    print(n, s)
    print(" ".join(map(str, times)))


if __name__ == "__main__":
    main()
