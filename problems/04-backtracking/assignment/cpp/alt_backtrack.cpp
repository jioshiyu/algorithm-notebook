// 选 5-13 工作分配（备选：回溯 + 最小剩余费用下界剪枝）
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n;
vector<vector<ll>> c;
ll best = LLONG_MAX;
vector<int> curPath, bestPath;
vector<char> used;

ll lowerBound(int i) {
    // 粗下界：剩余每个人至少付出其未占用工作中的最小费用
    ll s = 0;
    for (int k = i; k < n; ++k) {
        ll mn = LLONG_MAX;
        for (int j = 0; j < n; ++j)
            if (!used[j]) mn = min(mn, c[k][j]);
        s += mn;
    }
    return s;
}

void dfs(int i, ll cost) {
    if (cost + lowerBound(i) >= best) return;
    if (i == n) {
        best = cost;
        bestPath = curPath;
        return;
    }
    for (int j = 0; j < n; ++j) {
        if (used[j]) continue;
        used[j] = 1;
        curPath[i] = j + 1;
        dfs(i + 1, cost + c[i][j]);
        used[j] = 0;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    c.assign(n, vector<ll>(n));
    for (auto& row : c)
        for (auto& x : row) cin >> x;
    curPath.assign(n, 0);
    used.assign(n, 0);
    dfs(0, 0);
    cout << best << '\n';
    for (int i = 0; i < n; ++i) {
        if (i) cout << ' ';
        cout << bestPath[i];
    }
    cout << '\n';
    return 0;
}
