// 3-4 数字三角形（备选：自顶向下 DP，最后自底向上还原路径）
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<vector<long long>> a(n), dp(n);
    for (int i = 0; i < n; ++i) {
        a[i].resize(i + 1);
        dp[i].resize(i + 1);
        for (int j = 0; j <= i; ++j) cin >> a[i][j];
    }
    dp[0][0] = a[0][0];
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j <= i; ++j) {
            long long best = LLONG_MIN;
            if (j - 1 >= 0) best = max(best, dp[i - 1][j - 1]);
            if (j < i) best = max(best, dp[i - 1][j]);
            dp[i][j] = a[i][j] + best;
        }
    }
    int last = 0;
    for (int j = 1; j < n; ++j)
        if (dp[n - 1][j] > dp[n - 1][last]) last = j;

    vector<long long> path(n);
    int j = last;
    for (int i = n - 1; i >= 0; --i) {
        path[i] = a[i][j];
        if (i > 0) {
            if (j - 1 >= 0 && dp[i - 1][j - 1] + a[i][j] == dp[i][j]) --j;
            // 否则沿用 j（即来自 dp[i-1][j]）
        }
    }
    cout << dp[n - 1][last] << '\n';
    for (int i = 0; i < n; ++i) {
        if (i) cout << ' ';
        cout << path[i];
    }
    cout << '\n';
    return 0;
}
