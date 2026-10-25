"""暴力 / 独立参考解（用于对拍）。

- n <= 50000 时用逐个数数（朴素枚举）；
- 更大时用数位 DP（与主解的「逐位公式」是不同算法），保证对任意 n 可校验。
小 n 区域两种实现会互相校验，防止参考解自身出错。
"""

import sys
from functools import lru_cache


def naive(n: int) -> list[int]:
    cnt = [0] * 10
    for x in range(1, n + 1):
        for ch in str(x):
            cnt[ord(ch) - 48] += 1
    return cnt


def digit_dp(n: int, d: int) -> int:
    """数位 DP：统计 1..n（无前导零）中数字 d 的出现次数。"""
    if n <= 0:
        return 0
    s = [int(c) for c in str(n)]
    L = len(s)

    @lru_cache(maxsize=None)
    def dfs(pos: int, tight: bool, started: bool):
        if pos == L:
            return 0, 1  # (出现次数, 方案数)
        limit = s[pos] if tight else 9
        occ_total, paths_total = 0, 0
        for dig in range(limit + 1):
            ntight = tight and (dig == limit)
            if not started and dig == 0:
                occ, paths = dfs(pos + 1, ntight, False)
            else:
                occ, paths = dfs(pos + 1, ntight, True)
                if dig == d:
                    occ += paths
            occ_total += occ
            paths_total += paths
        return occ_total, paths_total

    return dfs(0, True, False)[0]


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    if n <= 50000:
        ref = naive(n)
        dp = [digit_dp(n, d) for d in range(10)]
        if ref != dp:
            raise SystemExit(f"参考解自检失败 n={n}: naive={ref} dp={dp}")
        out = ref
    else:
        out = [digit_dp(n, d) for d in range(10)]
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
