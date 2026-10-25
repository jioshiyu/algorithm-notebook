// 3-4 数字三角形
// 自底向上 DP：dp[i][j] = a[i][j] + max(dp[i+1][j], dp[i+1][j+1])
// 再从顶到底按 dp 较大者走，还原路径。
// 时间 O(n^2)，空间 O(n^2)。
//
// 输出：第一行最大路径和，第二行路径（n 个数，空格分隔）。
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<vector<long long>> a(n);
    for (int i = 0; i < n; ++i) {
        a[i].resize(i + 1);
        for (int j = 0; j <= i; ++j) cin >> a[i][j];
    }
    vector<vector<long long>> dp = a;
    for (int i = n - 2; i >= 0; --i)
        for (int j = 0; j <= i; ++j)
            dp[i][j] = a[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1]);

    vector<long long> path;
    int j = 0;
    for (int i = 0; i < n; ++i) {
        path.push_back(a[i][j]);
        if (i + 1 < n && dp[i + 1][j + 1] > dp[i + 1][j]) ++j;
    }
    cout << dp[0][0] << '\n';
    for (size_t k = 0; k < path.size(); ++k) {
        if (k) cout << ' ';
        cout << path[k];
    }
    cout << '\n';
    return 0;
}
