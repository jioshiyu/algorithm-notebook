// 5-3 最小重量机器设计（备选：按价格维度的 DP）
// dp[i][j] = 前 i 个部件、总价格恰为 j 时的最小重量；用 pre[i][j] 记录选择以还原。
// 时间 O(n * m * d)，空间 O(n * d)。d 很大时不适用（用主解分支限界）。
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    ll d;
    if (!(cin >> n >> m >> d)) return 0;
    vector<vector<ll>> c(n, vector<ll>(m)), w(n, vector<ll>(m));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) cin >> c[i][j];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) cin >> w[i][j];

    const ll INF = LLONG_MAX / 4;
    vector<vector<ll>> dp(n + 1, vector<ll>(d + 1, INF));
    vector<vector<int>> pre(n + 1, vector<int>(d + 1, -1));
    dp[0][0] = 0;
    for (int i = 0; i < n; ++i) {
        for (ll j = 0; j <= d; ++j) {
            if (dp[i][j] == INF) continue;
            for (int k = 0; k < m; ++k) {
                ll nj = j + c[i][k];
                if (nj > d) continue;
                ll nw = dp[i][j] + w[i][k];
                if (nw < dp[i + 1][nj]) {
                    dp[i + 1][nj] = nw;
                    pre[i + 1][nj] = k;
                }
            }
        }
    }
    ll best = INF;
    int bestJ = -1;
    for (ll j = 0; j <= d; ++j)
        if (dp[n][j] < best) best = dp[n][j], bestJ = (int)j;
    if (best == INF) {
        cout << "No solution\n";
        return 0;
    }
    vector<int> pick(n);
    int j = bestJ;
    for (int i = n; i >= 1; --i) {
        pick[i - 1] = pre[i][j] + 1;
        j -= c[i - 1][pre[i][j]];
    }
    cout << best << '\n';
    for (int i = 0; i < n; ++i) {
        if (i) cout << ' ';
        cout << pick[i];
    }
    cout << '\n';
    return 0;
}
