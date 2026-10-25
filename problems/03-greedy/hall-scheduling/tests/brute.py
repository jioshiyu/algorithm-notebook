"""暴力参考解：用事件扫描求最少会场数，再用 O(n^2) 分配给出可行方案。"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    acts = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n)]

    # 最少会场数 = 任意时刻同时进行的最大活动数（扫描线）
    events = []
    for s, e in acts:
        events.append((s, 1))
        events.append((e, -1))
    events.sort(key=lambda x: (x[0], x[1]))  # 同一时刻先结束时
    cur = best = 0
    for _, d in events:
        cur += d
        best = max(best, cur)

    # 分配：按开始时间排序，线性找第一个空闲的会场
    order = sorted(range(n), key=lambda i: (acts[i][0], acts[i][1]))
    free_at = []
    room = [0] * n
    for idx in order:
        s, e = acts[idx]
        pick = -1
        for r, t in enumerate(free_at):
            if t <= s:
                pick = r
                break
        if pick == -1:
            pick = len(free_at)
            free_at.append(e)
        else:
            free_at[pick] = e
        room[idx] = pick + 1
    print(best)
    print(" ".join(map(str, room)))


if __name__ == "__main__":
    main()
