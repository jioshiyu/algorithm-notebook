// 3-1 最长递增子序列（LIS）
// 贪心 + 二分：tail[len] 表示「长度恰为 len 的递增子序列的最小结尾值」，
// 用 lower_bound 找到当前元素应替换的位置，同时记录前驱以还原序列。
// 时间 O(n log n)，空间 O(n)。
//
// 输出：第一行长度，第二行一个最长递增子序列（空格分隔）。
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (auto& x : a) cin >> x;
    if (n == 0) {
        cout << "0\n\n";
        return 0;
    }

    vector<long long> tail;        // tail[k]: 长度 k+1 的最小结尾
    vector<int> tailIdx;           // 对应在 a 中的下标
    vector<int> pre(n, -1);        // 前驱下标

    for (int i = 0; i < n; ++i) {
        int pos = int(lower_bound(tail.begin(), tail.end(), a[i]) - tail.begin());
        if (pos == (int)tail.size()) {
            tail.push_back(a[i]);
            tailIdx.push_back(i);
        } else {
            tail[pos] = a[i];
            tailIdx[pos] = i;
        }
        if (pos > 0) pre[i] = tailIdx[pos - 1];
    }

    vector<int> path;
    for (int cur = tailIdx.back(); cur != -1; cur = pre[cur]) path.push_back(cur);
    reverse(path.begin(), path.end());

    cout << path.size() << '\n';
    for (size_t i = 0; i < path.size(); ++i) {
        if (i) cout << ' ';
        cout << a[path[i]];
    }
    cout << '\n';
    return 0;
}
