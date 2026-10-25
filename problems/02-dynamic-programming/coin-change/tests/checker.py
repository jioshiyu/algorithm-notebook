"""硬币 checker：最少枚数一致 + 方案金额与数量自洽。"""

import sys


def main() -> None:
    inp = open(sys.argv[1], "rb").read().split()
    n = int(inp[0])
    val = list(map(int, inp[1:1 + n]))
    cnt = list(map(int, inp[1 + n:1 + 2 * n]))
    m = int(inp[1 + 2 * n])

    exp = [ln for ln in open(sys.argv[2], encoding="utf-8").read().split("\n") if ln.strip()]
    got = [ln for ln in open(sys.argv[3], encoding="utf-8").read().split("\n") if ln.strip()]
    if not got:
        print("输出为空（程序可能崩溃）")
        raise SystemExit(1)
    if exp[0] == "No solution":
        if got[0] != "No solution":
            print(f"应无解，got: {got[0]}")
            raise SystemExit(1)
        print("OK")
        return
    if got[0] == "No solution":
        print(f"有解 {exp[0]}，got No solution")
        raise SystemExit(1)
    if int(got[0]) != int(exp[0]):
        print(f"最少枚数错误: got {got[0]}, expected {exp[0]}")
        raise SystemExit(1)
    total_sum = 0
    total_cnt = 0
    prev_v = -1
    for ln in got[1:]:
        v_s, c_s = ln.split()
        v, c = int(v_s), int(c_s)
        if v not in val:
            print(f"面值 {v} 不存在")
            raise SystemExit(1)
        i = val.index(v)
        if c < 0 or c > cnt[i]:
            print(f"面值 {v} 使用 {c} 枚超过库存 {cnt[i]}")
            raise SystemExit(1)
        if v <= prev_v:
            print("未按面值升序或重复输出")
            raise SystemExit(1)
        prev_v = v
        total_sum += v * c
        total_cnt += c
    if total_sum != m:
        print(f"方案金额 {total_sum} != {m}")
        raise SystemExit(1)
    if total_cnt != int(exp[0]):
        print(f"方案枚数 {total_cnt} != {exp[0]}")
        raise SystemExit(1)
    print("OK")


if __name__ == "__main__":
    main()
