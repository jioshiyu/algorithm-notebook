// 2-14 格雷码（Gray Code）
// 构造 n 位格雷码：长度 2^n 的序列，元素互不相同，相邻元素仅一位不同。
//
// 主解：位运算公式第 i 个码字为 i ^ (i >> 1)（二进制反射格雷码）。
// 备选：分治镜像构造 —— n 位由 n-1 位正序前加 0、逆序前加 1 拼接。
// 复杂度 O(n * 2^n)（输出规模本身），额外空间 O(1)（主解）。
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    long long total = 1LL << n;
    for (long long i = 0; i < total; ++i) {
        unsigned long long g = (unsigned long long)i ^ ((unsigned long long)i >> 1);
        for (int b = n - 1; b >= 0; --b) cout << ((g >> b) & 1ULL);
        cout << '\n';
    }
    return 0;
}
