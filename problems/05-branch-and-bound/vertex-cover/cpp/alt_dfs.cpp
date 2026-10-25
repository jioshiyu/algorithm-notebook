// 6-2 顶点覆盖（备选：回溯 DFS + 同样的下界剪枝）
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n, m;
vector<ll> w;
vector<pair<int, int>> edges;
ll best = LLONG_MAX;
vector<char> bestSel, curSel;

ll lowerBound() {
    // 极大匹配下界：互不相邻的未覆盖边，各取较小端点权
    vector<char> used(n, 0);
    ll sum = 0;
    for (auto [u, v] : edges) {
        if (curSel[u] || curSel[v]) continue;
        if (used[u] || used[v]) continue;
        used[u] = used[v] = 1;
        sum += min(w[u], w[v]);
    }
    return sum;
}

void dfs(int v, ll cost) {
    if (cost + lowerBound() >= best) return;
    if (v == n) {
        for (auto [u, vv] : edges)
            if (!curSel[u] && !curSel[vv]) return;
        best = cost;
        bestSel = curSel;
        return;
    }
    dfs(v + 1, cost);           // 不选
    curSel[v] = 1;
    dfs(v + 1, cost + w[v]);    // 选
    curSel[v] = 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> m)) return 0;
    w.resize(n);
    for (auto& x : w) cin >> x;
    edges.resize(m);
    for (auto& e : edges) {
        cin >> e.first >> e.second;
        --e.first;
        --e.second;
    }
    curSel.assign(n, 0);
    dfs(0, 0);
    cout << best << '\n';
    bool first = true;
    for (int i = 0; i < n; ++i) {
        if (bestSel[i]) {
            if (!first) cout << ' ';
            cout << i + 1;
            first = false;
        }
    }
    cout << '\n';
    return 0;
}
