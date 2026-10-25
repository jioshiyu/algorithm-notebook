// 4-1 会场安排问题
// n 个活动 [start, end)，用最少的会场安排全部活动（首尾相接可共用会场）。
// 主解：按开始时间排序，用最小堆维护「已占用会场的最早结束时间」；
//       若有会场 end <= 当前 start 则复用，否则新开一个。
// 时间 O(n log n)，空间 O(n)。
//
// 输出：第一行最少会场数 k；第二行 n 个整数，表示活动 i 的会场编号（1..k）。
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<pair<long long, long long>> acts(n);
    for (int i = 0; i < n; ++i) cin >> acts[i].first >> acts[i].second;
    vector<int> order(n);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int x, int y) {
        return acts[x].first < acts[y].first ||
               (acts[x].first == acts[y].first && acts[x].second < acts[y].second);
    });

    // 小根堆：(结束时间, 会场号)
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    vector<int> room(n);
    int k = 0;
    for (int idx : order) {
        auto [s, e] = acts[idx];
        if (!pq.empty() && pq.top().first <= s) {
            int r = pq.top().second;
            pq.pop();
            room[idx] = r;
            pq.push({e, r});
        } else {
            ++k;
            room[idx] = k;
            pq.push({e, k});
        }
    }
    cout << k << '\n';
    for (int i = 0; i < n; ++i) {
        if (i) cout << ' ';
        cout << room[i];
    }
    cout << '\n';
    return 0;
}
