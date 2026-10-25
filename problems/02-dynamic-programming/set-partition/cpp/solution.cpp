// 2-7 集合划分（Bell 数）
// 把 n 个不同元素划分为若干非空子集的方案数 B(n)。
// 主解：第二类 Stirling 数 S(n,k) 滚动一维 DP，B(n)=Σ_k S(n,k)。
//       S(n,k) = S(n-1,k-1) + k * S(n-1,k)
// 时间 O(n^2)，空间 O(n)。n <= 25 时 64 位整数足够（B(25) ≈ 4.6e18）。
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    if (n < 0) return 0;
    vector<unsigned long long> S(n + 1, 0);
    S[0] = 1;
    for (int i = 1; i <= n; ++i) {
        for (int k = i; k >= 1; --k) S[k] = S[k - 1] + (unsigned long long)k * S[k];
        S[0] = 0;
    }
    unsigned long long bell = 0;
    for (int k = 0; k <= n; ++k) bell += S[k];
    cout << bell << '\n';
    return 0;
}
