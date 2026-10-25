"""服务次序 checker：等待总时间正确 + 每个服务台上顺序合法（SPT、不重叠）。"""

import sys


def main() -> None:
    inp = open(sys.argv[1], "rb").read().split()
    n, s = int(inp[0]), int(inp[1])
    t = list(map(int, inp[2:2 + n]))

    exp = open(sys.argv[2], encoding="utf-8").read().strip().split("\n")
    got = [ln for ln in open(sys.argv[3], encoding="utf-8").read().split("\n") if ln.strip()]

    # 独立计算最优等待总时间（SPT + 线性扫描）
    order = sorted(range(n), key=lambda i: (t[i], i))
    free_at = [0] * (s + 1)
    exp_sum = 0
    for idx in order:
        pick = 1
        for r in range(2, s + 1):
            if free_at[r] < free_at[pick]:
                pick = r
        exp_sum += free_at[pick]
        free_at[pick] += t[idx]
    exp_avg = exp_sum / n

    got_avg = float(got[0])
    rows = []
    for ln in got[1:]:
        parts = ln.split()
        if len(parts) != 3:
            print(f"行格式错误: {ln}")
            raise SystemExit(1)
        rows.append((int(parts[0]), int(parts[1]), int(parts[2])))

    if len(rows) != n:
        print("行数不足")
        raise SystemExit(1)
    ids = sorted(r[0] for r in rows)
    if ids != list(range(1, n + 1)):
        print("客户编号不是 1..n")
        raise SystemExit(1)

    # 行按编号 1..n 输出，服务在行内给出，按编号索引
    srv = [0] * (n + 1)
    st = [0] * (n + 1)
    for cid, r, s0 in rows:
        srv[cid] = r
        st[cid] = s0

    sum_start = sum(st[1:])
    if sum_start != exp_sum:
        print(f"等待总时间错误: got {sum_start}, expected {exp_sum}")
        raise SystemExit(1)
    if abs(got_avg - round(exp_avg, 2)) > 0.011:
        print(f"平均等待时间错误: got {got_avg}, expected {exp_avg:.2f}")
        raise SystemExit(1)

    by_server = {}
    for cid in range(1, n + 1):
        if not (1 <= srv[cid] <= s):
            print(f"客户 {cid} 服务台编号越界")
            raise SystemExit(1)
        by_server.setdefault(srv[cid], []).append(cid)

    for r, ids_ in by_server.items():
        ids_.sort(key=lambda c: (st[c], c))
        clock = 0
        prev_t = -1
        for cid in ids_:
            if st[cid] != clock:
                print(f"服务台 {r}: 客户 {cid} 开始时刻应为 {clock}，实为 {st[cid]}")
                raise SystemExit(1)
            if prev_t > t[cid - 1]:
                print(f"服务台 {r}: 服务顺序不是最短优先（{prev_t} 后跟 {t[cid-1]}）")
                raise SystemExit(1)
            prev_t = t[cid - 1]
            clock += t[cid - 1]
    print("OK")


if __name__ == "__main__":
    main()
