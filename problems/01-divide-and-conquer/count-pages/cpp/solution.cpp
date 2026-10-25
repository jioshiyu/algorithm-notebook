// 1-1 统计数字问题
// 统计 1..n 的十进制写法（无前导零）中数字 0-9 各出现多少次。
//
// 逐位统计：固定一个数位 base（1,10,100,...），把 1..n 拆成
//     n = high * base * 10 + cur * base + low
// 该位上出现数字 d 的次数由 cur 与 d 的大小关系决定：
//     cur > d  : (high+1) * base
//     cur == d : high * base + low + 1
//     cur < d  : high * base
// d == 0 时要额外去掉「前导零」的贡献。
//
// 时间 O(log10 n)，空间 O(1)。n 最大 1e18 时用 long long 足够。
#include <bits/stdc++.h>
using namespace std;

using i64 = long long;

i64 countDigit(i64 n, int d) {
    i64 cnt = 0;
    i64 base = 1;
    while (base <= n) {
        i64 high = (base > n / 10) ? 0 : n / (base * 10);
        int cur = int((n / base) % 10);
        i64 low = n % base;
        if (d != 0) {
            if (cur > d) cnt += (high + 1) * base;
            else if (cur == d) cnt += high * base + low + 1;
            else cnt += high * base;
        } else {
            // 0 不能出现在最高位：high==0 时这一位全是前导零，直接跳过
            if (high > 0) {
                if (cur > 0) cnt += high * base;
                else cnt += (high - 1) * base + low + 1;
            }
        }
        if (base > LLONG_MAX / 10) break;  // n 接近 1e18 时防止 base 溢出
        base *= 10;
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    i64 n;
    if (!(cin >> n)) return 0;
    for (int d = 0; d <= 9; ++d) cout << countDigit(n, d) << '\n';
    return 0;
}
