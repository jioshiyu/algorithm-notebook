"""随机用例：python gen.py [seed] -> n m、权值、边（n <= 10）。"""

import random
import sys


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    n = rng.randint(1, 10)
    all_edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    rng.shuffle(all_edges)
    m = rng.randint(0, min(len(all_edges), 20)) if n > 1 else 0
    edges = all_edges[:m]
    lines = [f"{n} {m}"]
    lines.append(" ".join(str(rng.randint(1, 9)) for _ in range(n)))
    for u, v in edges:
        lines.append(f"{u + 1} {v + 1}")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
