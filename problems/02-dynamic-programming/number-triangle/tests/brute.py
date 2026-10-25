"""暴力参考解：枚举所有 2^(n-1) 条路径（小 n）。"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    a, p = [], 1
    for i in range(n):
        a.append(list(map(int, data[p:p + i + 1])))
        p += i + 1
    best_sum = None
    best_path = None
    stack = [(0, 0, [a[0][0]])]
    while stack:
        i, j, path = stack.pop()
        if i == n - 1:
            s = sum(path)
            if best_sum is None or s > best_sum:
                best_sum, best_path = s, path
            continue
        stack.append((i + 1, j, path + [a[i + 1][j]]))
        stack.append((i + 1, j + 1, path + [a[i + 1][j + 1]]))
    print(best_sum)
    print(" ".join(map(str, best_path)))


if __name__ == "__main__":
    main()
