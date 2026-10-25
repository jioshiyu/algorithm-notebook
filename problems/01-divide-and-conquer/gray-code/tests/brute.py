"""暴力/独立参考解：分治镜像构造 + 相邻性自检。"""

import sys


def gray(n: int) -> list[str]:
    if n == 1:
        return ["0", "1"]
    prev = gray(n - 1)
    cur = ["0" + s for s in prev]
    cur += ["1" + s for s in reversed(prev)]
    return cur


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    seq = gray(n)
    # 自检：长度、互异、相邻只差一位
    assert len(seq) == 1 << n, "长度不对"
    assert len(set(seq)) == len(seq), "存在重复码字"
    for a, b in zip(seq, seq[1:]):
        diff = sum(x != y for x, y in zip(a, b))
        assert diff == 1, f"相邻码字差异 {diff} 位: {a} {b}"
    sys.stdout.write("\n".join(seq) + "\n")


if __name__ == "__main__":
    main()
