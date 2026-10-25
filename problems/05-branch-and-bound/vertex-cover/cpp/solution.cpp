// 6-2 顶点覆盖（带权，最小权覆盖）
// 给定带权无向图，选一个顶点子集使每条边至少有一个端点被选，且权值和最小。
// 主解：分支限界（优先队列按下界升序扩展）。
//   下界 = 当前已选权值和 + 每条未覆盖边的 min(端点权值) 之和（可采纳）。
//   每个顶点只有「选 / 不选」两个分支。
//
// 输出：第一行最小总权值；第二行选中的顶点编号（升序，空格分隔）。
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<ll> w(n);
    for (auto& x : w) cin >> x;
    vector<int> eu(m), ev(m);
    int words = std::max(1, (m + 63) / 64);
    vector<vector<uint64_t>> inc(n, vector<uint64_t>(words, 0));
    for (int i = 0; i < m; ++i) {
        cin >> eu[i] >> ev[i];
        --eu[i];
        --ev[i];
        inc[eu[i]][i >> 6] |= 1ULL << (i & 63);
        inc[ev[i]][i >> 6] |= 1ULL << (i & 63);
    }

    // 下界：取一组「互不相邻」的未覆盖边（贪心极大匹配），
    // 每条匹配边至少需要选一个端点，代价 >= 该边两端较小权值。
    // 注意：直接对每条未覆盖边取 min 再相加不是合法下界（会重复计入共享顶点）。
    auto uncoveredBound = [&](const vector<uint64_t>& cov) {
        vector<char> used(n, 0);
        ll sum = 0;
        for (int i = 0; i < m; ++i) {
            if (((cov[i >> 6] >> (i & 63)) & 1ULL)) continue;
            int u = eu[i], v = ev[i];
            if (used[u] || used[v]) continue;
            used[u] = used[v] = 1;
            sum += min(w[u], w[v]);
        }
        return sum;
    };
    auto allCovered = [&](const vector<uint64_t>& cov) {
        for (int i = 0; i < m; ++i)
            if (!((cov[i >> 6] >> (i & 63)) & 1ULL)) return false;
        return true;
    };

    struct Node {
        int level;
        ll cost;
        vector<uint64_t> cov;
        vector<char> sel;
    };
    auto cmp = [](const Node& a, const Node& b) { return a.cost > b.cost; };
    priority_queue<Node, vector<Node>, decltype(cmp)> pq(cmp);

    Node root;
    root.level = 0;
    root.cost = 0;
    root.cov.assign(words, 0);
    root.sel.assign(n, 0);
    pq.push(root);

    ll best = LLONG_MAX;
    vector<char> bestSel(n, 0);

    while (!pq.empty()) {
        Node cur = pq.top();
        pq.pop();
        ll lb = cur.cost + uncoveredBound(cur.cov);
        if (lb >= best) continue;
        if (cur.level == n) {
            if (allCovered(cur.cov) && cur.cost < best) {
                best = cur.cost;
                bestSel = cur.sel;
            }
            continue;
        }
        int v = cur.level;
        // 分支 1：不选 v
        {
            Node nx = cur;
            nx.level = v + 1;
            if (nx.cost + uncoveredBound(nx.cov) < best) pq.push(std::move(nx));
        }
        // 分支 2：选 v
        {
            Node nx = cur;
            nx.level = v + 1;
            nx.cost += w[v];
            nx.sel[v] = 1;
            for (int k = 0; k < words; ++k) nx.cov[k] |= inc[v][k];
            if (nx.cost < best && nx.cost + uncoveredBound(nx.cov) < best) pq.push(std::move(nx));
        }
    }

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
