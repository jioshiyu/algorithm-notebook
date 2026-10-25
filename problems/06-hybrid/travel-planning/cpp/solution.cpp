// 大作业 旅行规划问题
// n 个景点（门票互不相同），要求恰好花完 target 元，求所有景点组合（每个景点最多去一次）。
// 主解：折半搜索（meet in the middle）—— 左半/右半分别枚举子集，右半按和分组，
//       对每个左子集查 target - sum 的右子集。时间复杂度 O(2^(n/2) * n)，n <= 40 可用。
//
// 输入：第一行 n target；第二行 n 个票价。
// 输出：第一行方案数；随后每行一个组合（景点编号升序，1-based）。
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

    int h = n / 2;
    auto enumerate = [&](int lo, int hi) {
        vector<pair<ll, int>> res;  // (和, mask)
        res.reserve(1 << (hi - lo));
        for (int mask = 0; mask < (1 << (hi - lo)); ++mask) {
            ll s = 0;
            for (int b = 0; b < hi - lo; ++b)
                if (mask >> b & 1) s += a[lo + b];
            res.push_back({s, mask});
        }
        return res;
    };
    auto left = enumerate(0, h);
    auto right = enumerate(h, n);
    unordered_map<ll, vector<int>> bySum;
    bySum.reserve(right.size() * 2);
    for (auto& [s, mask] : right) bySum[s].push_back(mask);

    vector<vector<int>> combos;
    for (auto& [ls, lmask] : left) {
        auto it = bySum.find(target - ls);
        if (it == bySum.end()) continue;
        for (int rmask : it->second) {
            vector<int> ids;
            for (int b = 0; b < h; ++b)
                if (lmask >> b & 1) ids.push_back(b + 1);
            for (int b = 0; b < n - h; ++b)
                if (rmask >> b & 1) ids.push_back(h + b + 1);
            sort(ids.begin(), ids.end());
            combos.push_back(std::move(ids));
        }
    }
    sort(combos.begin(), combos.end());
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
