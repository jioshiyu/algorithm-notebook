# GitHub 发布清单（用户侧操作）

> 仓库已本地完成：`D:\Projects\algorithm-notebook`，分支 `main`，所有改动已提交（最新 `a487d58` 之后的收尾提交）。
> 由于本机没有 `gh` CLI 与 GitHub token，**建仓库这一步需要你在网页完成**，之后推送由执行代理（我）完成。

## 1. 新建空仓库（1 分钟）

1. 打开 <https://github.com/new>
2. 填写：
   - **Repository name**: `algorithm-notebook`（如想改名，告诉执行代理即可）
   - **Description**: `算法专题笔记：分治 / DP / 贪心 / 回溯 / 分支限界 / 折半搜索，C++17 + Python 双实现，随机对拍验证`
   - **Visibility**: Public（推荐，用于开源展示；Private 也可先私有）
   - **不要**勾选 "Add a README file" / "Add .gitignore" / "Choose a license"（仓库里已有 LICENSE 与 README）
3. 点击 Create repository。

## 2. 通知执行代理

建好后直接回复一句「仓库建好了」，执行代理会执行：

```bash
cd D:\Projects\algorithm-notebook
git remote add origin https://github.com/jioshiyu/algorithm-notebook.git
git push -u origin main
```

推送使用本机 Git Credential Manager 已保存的 GitHub 凭据（与 workbench 仓库同一套），无需再次输入密码。

## 3. 推送后建议设置（可让执行代理代改文档）

- **About**：填描述；
- **Topics**：`algorithms` `cpp17` `python` `dynamic-programming` `greedy` `backtracking` `branch-and-bound` `meet-in-the-middle` `interview` `study-notes`；
- 如希望展示分类地图，可在 Settings → Pages 选择 `main` 分支根目录（当前无静态站点，可后续加 mkdocs）；
- CI：`.github/workflows/ci.yml` 会在首次 push 后自动运行（全题编译 + 对拍 + 结构检查）。

## 4. 备选：你自己推送

若你更想手动推送：

```bash
cd D:\Projects\algorithm-notebook
git remote add origin https://github.com/jioshiyu/algorithm-notebook.git
git push -u origin main
```

## 5. 发布前自检（执行代理已跑过）

- [x] 15 题 C++/Python 双实现，`python shared/check.py --all --stress 50` 全部通过
- [x] 每题 README、样例、暴力参考、随机生成器、必要 checker
- [x] CI、LICENSE（MIT）、.gitignore、docs 方法论/分类/进度/经验
- [x] 工作区干净、无临时文件、无编译产物入库
