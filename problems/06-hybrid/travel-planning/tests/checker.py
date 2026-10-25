"""旅行规划 checker：方案数一致 + 每个组合是合法且金额恰好 target 的子集。"""

import sys


def main() -> None:
    inp = open(sys.argv[1], "rb").read().split()
    n, target = int(inp[0]), int(inp[1])
    a = list(map(int, inp[2:2 + n]))

    got = [ln for ln in open(sys.argv[3], encoding="utf-8").read().split("\n") if ln.strip()]
    if not got:
        print("输出为空（程序可能崩溃）")
        raise SystemExit(1)
    count = int(got[0])
    combos = []
    for ln in got[1:]:
        ids = tuple(sorted(map(int, ln.split())))
        combos.append(ids)
    if count != len(combos):
        print(f"方案数 {count} 与行数 {len(combos)} 不一致")
        raise SystemExit(1)
    seen = set()
    for ids in combos:
        if any(not (1 <= x <= n) for x in ids):
            print(f"景点编号越界: {ids}")
            raise SystemExit(1)
        if ids in seen:
            print(f"重复方案: {ids}")
            raise SystemExit(1)
        seen.add(ids)
        s = sum(a[x - 1] for x in ids)
        if s != target:
            print(f"组合 {ids} 金额 {s} != {target}")
            raise SystemExit(1)

    # 独立枚举期望集合（n <= 18）
    exp = set()
    for mask in range(1 << n):
        s = 0
        ids = []
        for b in range(n):
            if mask >> b & 1:
                s += a[b]
                ids.append(b + 1)
        if s == target:
            exp.add(tuple(ids))
    if seen != exp:
        print(f"方案集合不一致: 多出 {len(seen - exp)} 个，缺少 {len(exp - seen)} 个")
        raise SystemExit(1)
    print("OK")


if __name__ == "__main__":
    main()
