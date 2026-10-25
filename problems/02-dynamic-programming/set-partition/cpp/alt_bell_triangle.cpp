// 2-7 集合划分（备选：Bell 三角）
// a[0][0]=1；每行首项 = 上一行末项；其余 = 左项 + 左上项。
// 第 n 行首项即 B(n)。时间 O(n^2)，空间 O(n)。
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<unsigned long long> prev(n + 1, 0), cur(n + 1, 0);
    prev[0] = 1;
    if (n == 0) {
        cout << 1 << '\n';
        return 0;
    }
    for (int i = 1; i <= n; ++i) {
        cur[0] = prev[i - 1];
        for (int j = 1; j <= i; ++j) cur[j] = cur[j - 1] + prev[j - 1];
        swap(prev, cur);
    }
    cout << prev[0] << '\n';
    return 0;
}
