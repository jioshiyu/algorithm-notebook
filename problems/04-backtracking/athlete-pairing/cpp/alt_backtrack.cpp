// 5-4 运动员最佳配对（备选：回溯 + 乐观上界剪枝）
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n;
vector<vector<ll>> P, Q;
ll bestSum = LLONG_MIN;
vector<int> bestPerm, curPerm;
vector<char> used;

// 剩余男运动员的乐观上界：每人取当前未占用女运动员中的最大优势（允许重复），
// 该上界 ≥ 真实可达值，可安全剪枝。
ll estimate(int t) {
    ll sum = 0;
    for (int i = t; i < n; ++i) {
        ll mx = LLONG_MIN;
        for (int j = 0; j < n; ++j)
            if (!used[j]) mx = max(mx, P[i][j] * Q[j][i]);
        sum += mx;
    }
    return sum;
}

void dfs(int t, ll curSum) {
    if (curSum + estimate(t) <= bestSum) return;
    if (t == n) {
        bestSum = curSum;
        bestPerm = curPerm;
        return;
    }
    for (int j = 0; j < n; ++j) {
        if (used[j]) continue;
        used[j] = 1;
        curPerm[t] = j;
        dfs(t + 1, curSum + P[t][j] * Q[j][t]);
        used[j] = 0;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    P.assign(n, vector<ll>(n));
    Q.assign(n, vector<ll>(n));
    for (auto& row : P)
        for (auto& x : row) cin >> x;
    for (auto& row : Q)
        for (auto& x : row) cin >> x;
    curPerm.assign(n, -1);
    used.assign(n, 0);
    dfs(0, 0);
    cout << bestSum << '\n';
    for (int i = 0; i < n; ++i) {
        if (i) cout << ' ';
        cout << bestPerm[i] + 1;
    }
    cout << '\n';
    return 0;
}
