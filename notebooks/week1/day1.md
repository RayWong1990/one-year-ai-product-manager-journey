# Week 1 - Day 1 学习记录

## 📌 今日目标

- [√] 完成本地开发环境搭建（Git, VS Code, Python）
- [√] 配置代理工具（Proxifier）解决网络问题
- [√] 成功拉取（或下载）项目到本地
- [√] 熟悉本地目录结构与初步操作（notebooks, projects, src）

## 🚀 今日进展

- [√] 安装 VS Code，配置基本插件（Python, GitLens等）
- [√] 安装 Python，并配置好环境变量
- [√] 安装 Git，测试本地版本
- [√] 配置 Anycast VPN，设置 SOCKS5 代理
- [√] 配置 Proxifier，使 Git 工具链走代理成功连接 GitHub
- [√] 成功拉取项目代码并在本地浏览
- [√] 创建 `notebooks/week1/day1.md` 学习笔记
- [√] 完成首次 Git commit，解决 push 失败、token配置、分支修正问题
- [√] 成功将 Day1 学习成果推送到 GitHub 仓库

## 🧠 GPT交互总结（与AI助手深度协作记录）

- 理解了为何最开始 `git` 无法识别：环境变量未完全生效，需在正确终端操作（Anaconda Prompt vs Powershell差异）
- 识别出 Proxifier规则优先级问题，确保 Git.exe、Code.exe 都走代理。
- 处理了 Git pull/push 过程中的多次报错，包括：
  - `src refspec main does not match any` → 需要创建本地main分支
  - `failed to connect server` → 配置 http.proxy
  - `error: failed to push some refs` → 需要先 git pull 或强制同步
- 学习了 Proxifier SOCKS5转发的细节（127.0.0.1:1080）
- 明确了 Git push 到 GitHub 需要 token（未来还需要配置 credential helper）
- 熟悉了最基本的 Git 提交标准动作（add-commit-push）
- 理解了本地未track文件和远程仓库同步冲突时的解决思路（git pull前处理）

## 💡 思考与收获

- 环境搭建比预期复杂，遇到问题要快速定位、逐步排除。
- VPN加速只是第一步，还需配合系统代理或进程代理（Proxifier细节管理）。
- Git基础操作（尤其是remote, branch, push, pull）在项目协作中至关重要。
- 第一次完整搭建起开发环境，体验到从零到一的成就感。
- 在 GPT 协助下，快速提升了排错效率，未来可以继续善用AI加速学习。

## 📅 明日计划

- 开启【第一周】学习主题：熟悉大模型基础、API调用流程
- 编写第一个 Echo Bot（src/目录下）
- 学习如何更规范地提交 Git commit（提交规范 Commit Message）

---

# 🗂️ 本地目录结构（初步）

```bash
one-year-ai-product-manager-journey/
│
├── notebooks/
│   ├── week1/
│       └── day1.md  # <--- 当前学习记录
│
├── projects/
│   └── (后续项目积累区)
│
├── src/
│   └── (后续小项目、Bot程序区)
│
├── .gitignore
├── LICENSE
└── README.md

Git Commit 操作记录
git add notebooks/week1/day1.md
git commit -m "feat: add Day1 learning record"
git push -u origin main

遇到冲突时处理步骤：
git pull origin main --allow-unrelated-histories
# or
git pull --rebase

📈 小结
✅ 本地环境已完成
✅ 网络代理配置正常
✅ Git基础技能掌握
✅ 成功同步第一份笔记
✅ 顺利完成 Day 1 起步！