"""随机用例：python gen.py [seed] -> n 与费用矩阵（n <= 8）。"""

import random
import sys


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    n = rng.randint(1, 8)
    lines = [str(n)]
    for _ in range(n):
        lines.append(" ".join(str(rng.randint(0, 20)) for _ in range(n)))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
