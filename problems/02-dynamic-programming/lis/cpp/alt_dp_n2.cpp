// 3-1 LIS 备选：O(n^2) 动态规划（暴力基准，考试可手写）
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (auto& x : a) cin >> x;
    vector<int> dp(n, 1), pre(n, -1);
    int best = 0, last = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (a[j] < a[i] && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                pre[i] = j;
            }
        }
        if (dp[i] > best) {
            best = dp[i];
            last = i;
        }
    }
    vector<long long> path;
    for (int cur = last; cur != -1; cur = pre[cur]) path.push_back(a[cur]);
    reverse(path.begin(), path.end());
    cout << path.size() << '\n';
    for (size_t i = 0; i < path.size(); ++i) {
        if (i) cout << ' ';
        cout << path[i];
    }
    cout << '\n';
    return 0;
}
