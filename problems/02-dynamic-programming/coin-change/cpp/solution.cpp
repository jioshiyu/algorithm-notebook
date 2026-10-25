// 选做 3-0 硬币问题（多重背包，求最少硬币数并输出方案）
// n 种面值 T[i]，每种最多用 coins[i] 枚，凑出金额 m，使硬币数最少。
//
// 主解：按面值逐层做「滑动窗口最小值」优化（单调队列），O(n*m)：
//   newdp[j] = min_{0<=k<=cnt} dp[j-k*v] + k
// 对每个余数类 r（j = r + x*v），令 y = x-k：
//   newdp[j] = x + min_{y in [x-cnt, x]}(dp[r+y*v] - y)
// 单调队列维护 dp[r+y*v] - y 的最小值，同时记录每个状态用了几枚该面值，便于还原方案。
//
// 输出：第一行最少硬币数；随后每行 "面值 枚数"（按面值升序）。凑不出输出 No solution。
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<ll> val(n);
    for (auto& x : val) cin >> x;
    vector<ll> cnt(n);
    for (auto& x : cnt) cin >> x;
    ll m;
    cin >> m;

    const ll INF = LLONG_MAX / 4;
    vector<ll> dp(m + 1, INF);
    dp[0] = 0;
    // used[i][j]：用前 i+1 种面值凑出 j 时，第 i 种面值用了几枚
    vector<vector<int>> used(n, vector<int>(m + 1, 0));

    for (int i = 0; i < n; ++i) {
        ll v = val[i];
        int c = (int)cnt[i];
        if (c <= 0 || v > m) continue;
        vector<ll> ndp(m + 1, INF);
        for (ll r = 0; r < v && r <= m; ++r) {
            deque<int> dq;  // 存放 x，按 dp[r+x*v]-x 单调递增
            for (int x = 0; r + (ll)x * v <= m; ++x) {
                ll j = r + (ll)x * v;
                if (dp[j] != INF) {
                    ll cur = dp[j] - x;
                    while (!dq.empty()) {
                        int bx = dq.back();
                        if (dp[r + (ll)bx * v] - bx >= cur) dq.pop_back();
                        else break;
                    }
                    dq.push_back(x);
                }
                while (!dq.empty() && dq.front() < x - c) dq.pop_front();
                if (!dq.empty()) {
                    int bx = dq.front();
                    ndp[j] = dp[r + (ll)bx * v] + (x - bx);
                    used[i][j] = x - bx;
                }
            }
        }
        dp.swap(ndp);
    }

    if (dp[m] == INF) {
        cout << "No solution\n";
        return 0;
    }
    vector<ll> use(n, 0);
    ll j = m;
    for (int i = n - 1; i >= 0; --i) {
        ll k = used[i][j];
        use[i] = k;
        j -= k * val[i];
    }
    cout << dp[m] << '\n';
    for (int i = 0; i < n; ++i)
        if (use[i]) cout << val[i] << ' ' << use[i] << '\n';
    return 0;
}
