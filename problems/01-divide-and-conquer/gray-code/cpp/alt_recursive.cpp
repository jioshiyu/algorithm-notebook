// 2-14 格雷码（分治镜像构造，备选解）
// 第 n 位格雷码 = [0 + G(n-1) 正序] 拼接 [1 + G(n-1) 逆序]。
// 时间 O(2^n)，空间 O(2^n)。
#include <bits/stdc++.h>
using namespace std;

static vector<string> gray(int n) {
    if (n == 1) return {"0", "1"};
    vector<string> prev = gray(n - 1);
    vector<string> cur;
    cur.reserve(prev.size() * 2);
    for (const string& s : prev) cur.push_back("0" + s);
    for (int i = (int)prev.size() - 1; i >= 0; --i) cur.push_back("1" + prev[i]);
    return cur;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    for (const string& s : gray(n)) cout << s << '\n';
    return 0;
}
