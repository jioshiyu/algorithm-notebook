// 选做 3-0 硬币问题（备选：逐面值多重背包 DP，O(n·m·count)），适合小规模与讲解
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<ll> val(n), cnt(n);
    for (auto& x : val) cin >> x;
    for (auto& x : cnt) cin >> x;
    ll m;
    cin >> m;
    const ll INF = LLONG_MAX / 4;

    // dp[i][j]: 前 i 种面值凑 j 的最少硬币数
    vector<vector<ll>> dp(n + 1, vector<ll>(m + 1, INF));
    vector<vector<ll>> take(n + 1, vector<ll>(m + 1, -1));
    dp[0][0] = 0;
    for (int i = 1; i <= n; ++i) {
        for (ll j = 0; j <= m; ++j) {
            if (dp[i - 1][j] == INF) continue;
            for (ll k = 0; k <= cnt[i - 1] && j + k * val[i - 1] <= m; ++k) {
                ll nj = j + k * val[i - 1];
                ll nc = dp[i - 1][j] + k;
                if (nc < dp[i][nj]) {
                    dp[i][nj] = nc;
                    take[i][nj] = k;
                }
            }
        }
    }
    if (dp[n][m] == INF) {
        cout << "No solution\n";
        return 0;
    }
    vector<ll> used(n, 0);
    ll j = m;
    for (int i = n; i >= 1; --i) {
        ll k = take[i][j];
        used[i - 1] = k;
        j -= k * val[i - 1];
    }
    cout << dp[n][m] << '\n';
    for (int i = 0; i < n; ++i)
        if (used[i]) cout << val[i] << ' ' << used[i] << '\n';
    return 0;
}
