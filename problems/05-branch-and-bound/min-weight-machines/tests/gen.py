"""随机用例：python gen.py [seed] -> n m d 与价格/重量矩阵。"""

import random
import sys


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    n = rng.randint(1, 5)
    m = rng.randint(1, 3)
    d = rng.randint(1, 30)
    lines = [f"{n} {m} {d}"]
    prices = [[rng.randint(0, 10) for _ in range(m)] for _ in range(n)]
    weights = [[rng.randint(0, 9) for _ in range(m)] for _ in range(n)]
    for row in prices:
        lines.append(" ".join(map(str, row)))
    for row in weights:
        lines.append(" ".join(map(str, row)))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
