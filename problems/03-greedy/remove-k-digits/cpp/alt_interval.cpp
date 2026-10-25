// 选 4-11 删数问题（备选：区间贪心 —— 每次在可选区间里选最小的非零数字作为下一位）
// 时间 O(n·k)，适合 n 较小或用于讲解贪心选择。
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string num;
    int k;
    if (!(cin >> num)) return 0;
    cin >> k;
    int n = (int)num.size();
    int m = n - k;  // 需要保留的位数
    if (m <= 0) {
        cout << "0\n";
        return 0;
    }
    string res;
    int start = 0;
    for (int i = 0; i < m; ++i) {
        int end = k + i;  // 第 i 位最多取到这里
        char best = '9' + 1;
        int bestPos = -1;
        for (int j = start; j <= end; ++j) {
            if (i == 0 && num[j] == '0') continue;  // 首位不能是 0
            if (num[j] < best) {
                best = num[j];
                bestPos = j;
            }
        }
        if (bestPos == -1) {
            cout << "0\n";
            return 0;
        }
        res.push_back(best);
        start = bestPos + 1;
    }
    cout << res << '\n';
    return 0;
}
