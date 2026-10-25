// 选做 2-1 众数
// 给定多重集合，求重数最大的元素（众数）及其重数。
// 约定：若有多个众数，输出数值最小者，保证结果确定。
// 主解：排序 + 一次扫描，O(n log n)。
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
        cout << "0 0\n";
        return 0;
    }
    sort(a.begin(), a.end());
    long long bestVal = a[0], bestCnt = 1;
    long long curVal = a[0], curCnt = 1;
    for (int i = 1; i < n; ++i) {
        if (a[i] == curVal) {
            ++curCnt;
        } else {
            curVal = a[i];
            curCnt = 1;
        }
        // 扫描顺序是从小到大：只有严格更大才替换，平手保留更小值
        if (curCnt > bestCnt) {
            bestCnt = curCnt;
            bestVal = curVal;
        }
    }
    cout << bestVal << '\n' << bestCnt << '\n';
    return 0;
}
