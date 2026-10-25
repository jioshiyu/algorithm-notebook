// 选 4-11 删数问题
// 给定十进制数字串 num 与 k，删除 k 个数字，使剩下的数字按原顺序组成的数最小。
// 主解：单调栈 —— 从左到右扫描，若栈顶数字 > 当前数字且还能删，则弹出（删掉更大的一位）。
// 时间 O(n)，空间 O(n)。
//
// 输入：第一行数字串 num，第二行 k。
// 输出：最小数（去掉前导零；若为空输出 0）。
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string num;
    int k;
    if (!(cin >> num)) return 0;
    cin >> k;
    string st;
    for (char ch : num) {
        while (k > 0 && !st.empty() && st.back() > ch) {
            st.pop_back();
            --k;
        }
        st.push_back(ch);
    }
    while (k > 0 && !st.empty()) {
        st.pop_back();
        --k;
    }
    size_t pos = st.find_first_not_of('0');
    string ans = (pos == string::npos) ? "0" : st.substr(pos);
    cout << ans << '\n';
    return 0;
}
