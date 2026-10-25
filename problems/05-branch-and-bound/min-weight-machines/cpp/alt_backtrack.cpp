// 5-3 最小重量机器设计（备选：回溯法 DFS + 双剪枝）
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n, m;
ll d;
vector<vector<ll>> c, w;
ll bestW = LLONG_MAX;
vector<int> curPath, bestPath;

void dfs(int i, ll curC, ll curW) {
    if (curW >= bestW) return;
    if (i == n) {
        bestW = curW;
        bestPath = curPath;
        return;
    }
    for (int j = 0; j < m; ++j) {
        ll nc = curC + c[i][j];
        if (nc > d) continue;
        curPath.push_back(j + 1);
        dfs(i + 1, nc, curW + w[i][j]);
        curPath.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> m >> d)) return 0;
    c.assign(n, vector<ll>(m));
    w.assign(n, vector<ll>(m));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) cin >> c[i][j];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) cin >> w[i][j];

    dfs(0, 0, 0);
    if (bestW == LLONG_MAX) {
        cout << "No solution\n";
    } else {
        cout << bestW << '\n';
        for (int i = 0; i < n; ++i) {
            if (i) cout << ' ';
            cout << bestPath[i];
        }
        cout << '\n';
    }
    return 0;
}
