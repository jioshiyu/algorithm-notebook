// 4-1 会场安排（备选：线性扫描会场空闲时间 O(n^2)，适合 n 较小或面试手写）
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
        return acts[x].first < acts[y].first;
    });

    vector<long long> freeAt;  // 每个会场的空闲时刻
    vector<int> room(n);
    for (int idx : order) {
        auto [s, e] = acts[idx];
        int pick = -1;
        for (int r = 0; r < (int)freeAt.size(); ++r) {
            if (freeAt[r] <= s) {
                pick = r;
                break;
            }
        }
        if (pick == -1) {
            pick = (int)freeAt.size();
            freeAt.push_back(e);
        } else {
            freeAt[pick] = e;
        }
        room[idx] = pick + 1;
    }
    cout << freeAt.size() << '\n';
    for (int i = 0; i < n; ++i) {
        if (i) cout << ' ';
        cout << room[i];
    }
    cout << '\n';
    return 0;
}
