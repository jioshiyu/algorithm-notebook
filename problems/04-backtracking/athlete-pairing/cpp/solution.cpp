// 5-4 运动员最佳配对
// n 名男运动员、n 名女运动员：男 i 与女 j 配对的双打优势为 P[i][j] * Q[j][i]。
// 求一个配对方案使总优势最大。
// 主解：状压 DP —— dp[mask] = 已给前 popcount(mask) 名男运动员配完、占用女运动员集合为 mask 时的最大总优势。
//       时间 O(n * 2^n)，空间 O(2^n)。n <= 15 可用。
//
// 输出：第一行最大总优势；第二行 n 个整数，男 i 配的女运动员编号（1..n）。
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<vector<ll>> P(n, vector<ll>(n)), Q(n, vector<ll>(n));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) cin >> P[i][j];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) cin >> Q[i][j];

    int full = 1 << n;
    const ll NEG = LLONG_MIN / 4;
    vector<ll> dp(full, NEG);
    vector<int> pre(full, -1);
    vector<unsigned char> pc(full, 0);
    for (int mask = 1; mask < full; ++mask) pc[mask] = pc[mask >> 1] + (mask & 1);
    dp[0] = 0;

    for (int mask = 0; mask < full; ++mask) {
        if (dp[mask] == NEG) continue;
        int i = pc[mask];  // 下一个待配对的男运动员
        if (i == n) continue;
        for (int j = 0; j < n; ++j) {
            if (mask & (1 << j)) continue;
            int nm = mask | (1 << j);
            ll cand = dp[mask] + P[i][j] * Q[j][i];
            if (cand > dp[nm]) {
                dp[nm] = cand;
                pre[nm] = j;
            }
        }
    }

    int mask = full - 1;
    vector<int> match(n);
    for (int i = n - 1; i >= 0; --i) {
        int j = pre[mask];
        match[i] = j + 1;
        mask ^= (1 << j);
    }
    cout << dp[full - 1] << '\n';
    for (int i = 0; i < n; ++i) {
        if (i) cout << ' ';
        cout << match[i];
    }
    cout << '\n';
    return 0;
}
