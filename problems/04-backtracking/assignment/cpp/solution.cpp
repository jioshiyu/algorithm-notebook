// 选 5-13 工作分配问题
// n 个人、n 件工作，c[i][j] 为第 i 人做第 j 件工作的费用；每人恰好一件、每件恰好一人，使总费用最小。
// 主解：状压 DP —— dp[mask] = 已给前 popcount(mask) 个人分配完、占用工作集合为 mask 时的最小费用。
// 时间 O(n·2^n)，空间 O(2^n)。n <= 15 可用。
//
// 输出：第一行最小总费用；第二行 n 个整数（第 i 人分配的工作编号 1..n）。
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<vector<ll>> c(n, vector<ll>(n));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) cin >> c[i][j];

    int full = 1 << n;
    vector<ll> dp(full, LLONG_MAX / 4);
    vector<int> pre(full, -1);
    vector<unsigned char> pc(full, 0);
    for (int mask = 1; mask < full; ++mask) pc[mask] = pc[mask >> 1] + (mask & 1);
    dp[0] = 0;
    for (int mask = 0; mask < full; ++mask) {
        if (dp[mask] >= LLONG_MAX / 8) continue;
        int i = pc[mask];
        if (i == n) continue;
        for (int j = 0; j < n; ++j) {
            if (mask & (1 << j)) continue;
            int nm = mask | (1 << j);
            ll cand = dp[mask] + c[i][j];
            if (cand < dp[nm]) {
                dp[nm] = cand;
                pre[nm] = j;
            }
        }
    }
    int mask = full - 1;
    vector<int> pick(n);
    for (int i = n - 1; i >= 0; --i) {
        int j = pre[mask];
        pick[i] = j + 1;
        mask ^= (1 << j);
    }
    cout << dp[full - 1] << '\n';
    for (int i = 0; i < n; ++i) {
        if (i) cout << ' ';
        cout << pick[i];
    }
    cout << '\n';
    return 0;
}
