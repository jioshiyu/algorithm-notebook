"""4-1 会场安排（Python 版，贪心 + 小根堆）。"""

import heapq
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    acts = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n)]
    order = sorted(range(n), key=lambda i: (acts[i][0], acts[i][1]))

    pq = []  # (end, room)
    room = [0] * n
    k = 0
    for idx in order:
        s, e = acts[idx]
        if pq and pq[0][0] <= s:
            end, r = heapq.heappop(pq)
            room[idx] = r
            heapq.heappush(pq, (e, r))
        else:
            k += 1
            room[idx] = k
            heapq.heappush(pq, (e, k))
    sys.stdout.write(str(k) + "\n" + " ".join(map(str, room)) + "\n")


if __name__ == "__main__":
    main()
