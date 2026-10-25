"""会场安排 checker：会场数一致 + 同一会场内活动不重叠 + 编号范围合法。"""

import sys


def main() -> None:
    inp = open(sys.argv[1], "rb").read().split()
    n = int(inp[0])
    acts = [(int(inp[1 + 2 * i]), int(inp[2 + 2 * i])) for i in range(n)]

    exp_k = int(open(sys.argv[2], encoding="utf-8").read().split()[0])
    got = open(sys.argv[3], encoding="utf-8").read().split()
    got_k = int(got[0])
    room = list(map(int, got[1:1 + n]))

    if got_k != exp_k:
        print(f"会场数错误: got {got_k}, expected {exp_k}")
        raise SystemExit(1)
    if len(room) != n:
        print("会场编号个数不足")
        raise SystemExit(1)
    if any(r < 1 or r > got_k for r in room):
        print("会场编号越界")
        raise SystemExit(1)

    by_room = {}
    for i, r in enumerate(room):
        by_room.setdefault(r, []).append(i)
    for r, ids in by_room.items():
        ids.sort(key=lambda i: acts[i][0])
        for a, b in zip(ids, ids[1:]):
            if acts[a][1] > acts[b][0]:
                print(f"会场 {r} 内活动冲突: {acts[a]} 与 {acts[b]}")
                raise SystemExit(1)
    print("OK")


if __name__ == "__main__":
    main()
