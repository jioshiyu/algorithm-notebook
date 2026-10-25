"""随机用例：python gen.py [seed] -> 数字串与 k。"""

import random
import sys


def main() -> None:
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    n = rng.randint(1, 12)
    s = "".join(rng.choice("0123456789") for _ in range(n))
    if s[0] == "0":
        s = "1" + s[1:]
    k = rng.randint(0, n)
    print(s)
    print(k)


if __name__ == "__main__":
    main()
