// 大作业 旅行规划（备选：回溯 + 约束剪枝）
// 景点票价为正，按原顺序做「选 / 不选」DFS；一旦和达到 target 就记录（再加只会更大）。
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n;
ll target;
vector<ll> a;
vector<vector<int>> combos;
vector<int> cur;

void dfs(int i, ll sum) {
    if (sum == target) {
        combos.push_back(cur);
        return;
    }
    if (i == n || sum > target) return;
    dfs(i + 1, sum);                       // 不选 i
    cur.push_back(i + 1);
    dfs(i + 1, sum + a[i]);                // 选 i
    cur.pop_back();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> target)) return 0;
    a.resize(n);
    for (auto& x : a) cin >> x;
    dfs(0, 0);
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
