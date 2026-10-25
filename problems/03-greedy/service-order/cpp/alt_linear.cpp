// 4-7 多处最优服务次序（备选：线性扫描服务台空闲时间 O(n^2)）
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
    sort(order.begin(), order.end(), [&](int a, int b) { return t[a] < t[b]; });

    vector<long long> freeAt(s + 1, 0);
    vector<int> srv(n);
    vector<long long> start(n);
    long long sumStart = 0;
    for (int id : order) {
        int pick = 1;
        for (int r = 2; r <= s; ++r)
            if (freeAt[r] < freeAt[pick]) pick = r;
        srv[id] = pick;
        start[id] = freeAt[pick];
        sumStart += freeAt[pick];
        freeAt[pick] += t[id];
    }
    cout << fixed << setprecision(2) << (double)sumStart / n << '\n';
    for (int i = 0; i < n; ++i) cout << i + 1 << ' ' << srv[i] << ' ' << start[i] << '\n';
    return 0;
}
