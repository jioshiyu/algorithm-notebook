"""随机用例：python gen.py [seed] -> n 与 n 个区间（含首尾相接）。"""

import random
import sys


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    n = rng.randint(1, 120)
    lines = [str(n)]
    for _ in range(n):
        s = rng.randint(0, 60)
        e = s + rng.randint(1, 20)
        lines.append(f"{s} {e}")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
