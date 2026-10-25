// 大作业 旅行规划（备选：直接枚举 2^n，n <= 20 时简单直观）
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    ll target;
    if (!(cin >> n >> target)) return 0;
    vector<ll> a(n);
    for (auto& x : a) cin >> x;
    vector<vector<int>> combos;
    for (int mask = 0; mask < (1 << n); ++mask) {
        ll s = 0;
        vector<int> ids;
        for (int b = 0; b < n; ++b)
            if (mask >> b & 1) {
                s += a[b];
                ids.push_back(b + 1);
            }
        if (s == target) combos.push_back(ids);
    }
    cout << combos.size() << '\n';
    for (auto& ids : combos) {
        for (size_t i = 0; i < ids.size(); ++i) {
            if (i) cout << ' ';
            cout << ids[i];
        }
        cout << '\n';
    }
    return 0;
}
