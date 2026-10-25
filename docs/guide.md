# 使用指南（目录约定 · 运行方式 · 扩题流程）

## 1. 仓库结构

```
algorithm-notebook/
├── README.md                  # 门面：定位、导航、题目总表
├── LICENSE
├── shared/
│   └── check.py               # 通用质检：编译 / 样例 / 随机对拍 / 计时
├── docs/
│   ├── categories.md          # 分类地图（按算法思想）
│   ├── methodology.md         # 五步法与优化检查单
│   ├── progress.md            # 进度与 token 消耗台账
│   └── roadmap.md             # 扩建计划
└── problems/
    └── <分类>/<slug>/
        ├── README.md          # 题解（统一结构）
        ├── cpp/
        │   ├── solution.cpp   # 主解
        │   └── alt_*.cpp      # 备选解（可选）
        ├── python/
        │   └── solution.py
        └── tests/
            ├── samples/       # *.in / *.out
            ├── gen.py         # 随机用例生成器（stdout 输出输入）
            └── brute.py       # 暴力参考解（stdin → stdout）
```

## 2. 运行约定

- **输入输出只用 stdin/stdout**：不读文件、不写死路径，便于对拍与跨平台；
- C++：`g++ -O2 -std=c++17`，`solution.cpp` 自带 `main`；
- Python：≥ 3.10，`solution.py` 自带 `main`，只用标准库；
- 样例格式：`tests/samples/<name>.in` 与同名 `.out`，每题至少一个样例；
- 测试生成器 `gen.py`：`python gen.py [seed]` 打印一个用例；
- 暴力解 `brute.py`：读取 stdin，打印期望输出（允许慢，但要绝对正确）；
- **多解/方案题的 `tests/checker.py`**：接口为
  `python checker.py <input> <expected> <got>`，退出码 0 表示通过，否则打印原因。
  适用于「答案不唯一」的题（LIS 任一条、三角形路径、分配方案、覆盖方案、集合组合）。

## 3. 一题全检

```bash
python shared/check.py problems/<分类>/<slug> --stress 500
```

执行顺序：

1. 编译 `cpp/solution.cpp`（找不到编译器时自动跳过 C++ 部分并提示）；
2. 逐样例比对输出；
3. 用 `gen.py` 生成随机用例，分别运行 C++/Python 解与 `brute.py` 对拍；
4. 统计单次耗时，失败时保留失败用例（写入 `tests/tmp/`）便于复现。

## 4. 新增一题的流程

1. 在 `problems/<分类>/` 下建 `<slug>/`，slug 用英文小写加连字符（如 `count-pages`）；
2. 写 `tests/samples/` 最小样例（至少包含边界用例）；
3. 写 `tests/brute.py`（先有暴力，再有优化）；
4. 写 `cpp/solution.cpp` 与 `python/solution.py`，使两者通过全部样例；
5. 跑 `shared/check.py --stress 500` 直到全绿；
6. 按 [methodology.md](methodology.md) 写 `README.md`；
7. 更新 `docs/categories.md` 与 `docs/progress.md`，并在根 README 的题目总表打 ✅。

## 5. 代码规范

- C++：`#include <bits/stdc++.h>` 可接受（面向刷题场景），变量命名用 `lowerCamel` 或短名；函数上写一句注释说明「算法 + 复杂度」；
- Python：标准库优先，`sys.stdin.buffer.read()` 读入，避免 `input()` 逐行开销；
- 多解：主解用最推荐的写法；其它写法放 `alt_*.cpp` / `python/alt_*.py`，在 README 的多解对比表里列明适用场景。

## 6. 文档规范

每题 README 固定小节（顺序固定，便于批量阅读）：

1. 题目（含输入输出格式与约束）
2. 直观想法与暴力
3. 优化思路（如何从暴力到目标复杂度，关键观察）
4. 正确性要点
5. 复杂度
6. 一题多解对比表
7. 易错点与边界
8. 测试与对拍说明
9. 复习要点（一句话）
10. 关联题目与延伸
