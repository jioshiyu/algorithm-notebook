// 选做 2-1 众数（备选：哈希计数），O(n) 平均时间。
// 平手时取数值最小的众数，保证与主解一致。
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    unordered_map<long long, int> freq;
    freq.reserve(n * 2);
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        ++freq[x];
    }
    long long bestVal = 0, bestCnt = -1;
    for (auto& [v, c] : freq) {
        if (c > bestCnt || (c == bestCnt && v < bestVal) || bestCnt < 0) {
            bestCnt = c;
            bestVal = v;
        }
    }
    cout << bestVal << '\n' << bestCnt << '\n';
    return 0;
}
