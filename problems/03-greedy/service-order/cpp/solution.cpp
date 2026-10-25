// 4-7 多处最优服务次序问题
// n 个客户同时到达，服务时间 t_i；s 个服务台。求使平均等待时间最小的安排。
// 贪心：把客户按服务时间升序排序；每个客户交给最早空闲的服务台。
// 时间 O(n log n + n log s)，空间 O(n + s)。
//
// 输出：第一行平均等待时间（保留两位小数）；
//       随后 n 行：客户编号 服务台编号 开始服务时刻（客户按编号 1..n）。
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, s;
    if (!(cin >> n >> s)) return 0;
    vector<long long> t(n);
    for (auto& x : t) cin >> x;

    vector<int> order(n);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int a, int b) {
        return t[a] < t[b] || (t[a] == t[b] && a < b);
    });

    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    for (int r = 1; r <= s; ++r) pq.push({0, r});
    vector<int> srv(n);
    vector<long long> start(n);
    long long sumStart = 0;
    for (int id : order) {
        auto [freeAt, r] = pq.top();
        pq.pop();
        srv[id] = r;
        start[id] = freeAt;
        sumStart += freeAt;
        pq.push({freeAt + t[id], r});
    }
    cout << fixed << setprecision(2) << (double)sumStart / n << '\n';
    for (int i = 0; i < n; ++i)
        cout << i + 1 << ' ' << srv[i] << ' ' << start[i] << '\n';
    return 0;
}
