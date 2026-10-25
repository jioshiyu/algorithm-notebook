"""选 4-11 删数问题（Python 版，单调栈）。"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    num = data[0].decode()
    k = int(data[1])
    st = []
    for ch in num:
        while k > 0 and st and st[-1] > ch:
            st.pop()
            k -= 1
        st.append(ch)
    if k > 0:
        st = st[:-k]
    ans = "".join(st).lstrip("0")
    print(ans if ans else "0")


if __name__ == "__main__":
    main()
