// 5-3 / 选 6-4 最小重量机器设计（合并两道实验报告，三种范式对照）
// n 个部件，每个部件从 m 个供应商中选一个；价格 c[i][j]、重量 w[i][j]；
// 总价格不超过 d 时，使总重量最小。
//
// 主解：分支限界。—— 优先级队列按「当前重量 + 剩余部件最小重量和」升序扩展，
// 配合价格约束剪枝与重量上界剪枝，能在大 d 时工作。
// 备选：动态规划（按价格维度）与回溯法（DFS + 剪枝），见 alt_*.cpp。
//
// 输出：第一行最小重量；第二行 n 个整数（每个部件选的供应商编号 1..m）。
//       无解输出 No solution。
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

    // suffix[i] = 部件 i..n-1 每个都取最小重量时的重量和（可采纳下界）
    vector<ll> suffix(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
        ll mn = LLONG_MAX;
        for (int j = 0; j < m; ++j) mn = min(mn, w[i][j]);
        suffix[i] = suffix[i + 1] + mn;
    }

    struct Node {
        int level;
        ll cost, weight;
        vector<int> pick;
    };
    auto worse = [&](const Node& a, const Node& b) {
        // 小根堆：下界小者先出
        return a.weight + suffix[a.level] > b.weight + suffix[b.level];
    };
    priority_queue<Node, vector<Node>, decltype(worse)> pq(worse);

    ll bestW = LLONG_MAX;
    vector<int> bestPick;
    pq.push({0, 0, 0, {}});

    while (!pq.empty()) {
        Node cur = pq.top();
        pq.pop();
        if (cur.weight + suffix[cur.level] >= bestW) continue;
        if (cur.level == n) {
            if (cur.cost <= d && cur.weight < bestW) {
                bestW = cur.weight;
                bestPick = cur.pick;
            }
            continue;
        }
        int i = cur.level;
        for (int j = 0; j < m; ++j) {
            ll nc = cur.cost + c[i][j];
            ll nw = cur.weight + w[i][j];
            if (nc > d) continue;
            if (nw + suffix[i + 1] >= bestW) continue;
            Node nx;
            nx.level = i + 1;
            nx.cost = nc;
            nx.weight = nw;
            nx.pick = cur.pick;
            nx.pick.push_back(j + 1);
            pq.push(std::move(nx));
        }
    }

    if (bestW == LLONG_MAX) {
        cout << "No solution\n";
    } else {
        cout << bestW << '\n';
        for (int k = 0; k < n; ++k) {
            if (k) cout << ' ';
            cout << bestPick[k];
        }
        cout << '\n';
    }
    return 0;
}
