"""2-14 格雷码（Python 版，位运算公式）。"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    total = 1 << n
    out = []
    for i in range(total):
        g = i ^ (i >> 1)
        out.append(format(g, f"0{n}b"))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
