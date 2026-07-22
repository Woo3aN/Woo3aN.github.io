# 博客更新日志

## 2026-07-22

### Vercount 统计
- 切换到 Vercount 替代不蒜子（`busuanzi` CDN → `events.vercount.one/js`）
- 发现 Vercount `site_pv` 每天重置（后端 bug，非配置问题）
- GitHub Actions 移除 `hexo clean`，减少触发数据重置的可能

### SEO
- 添加 `robots.txt`，声明 Google 和 Baidu sitemap
- `_config.yml` 补充 `description` 和 `keywords`
- Bing Webmaster Tools 验证成功，提交 sitemap
- 百度站长平台无法添加（github.io 域名名额已满）

### 界面
- 菜单「关于」→「About」
- 搜索按钮文字「搜索」→「Search」
- Archives 页面大标题「Archives」→「归档」（与 Tags「标签」、Categories「分类」统一）
- 归档页按月分组（2026 → 2026年07月）
- 搜索弹窗标题保留中文「搜索」，输入框保留中文

### 日期修复
- 文章日期统一加 `12:00` 时间戳，避免 UTC 时区导致日期回退一天
- GitHub Actions 智能日期：文章内容未变则沿用旧日期，改配置不刷文章日期
- `_config.yml` 时区注释掉，Actions 设 `TZ: Asia/Shanghai`

### PJAX
- 关闭 PJAX（与 Vercount 冲突待修复）

### 部署
- Node.js 22，GitHub Actions 自动部署
- `fetch-depth: 0` + git 历史恢复文件修改时间

---

## 2026-07-15 ~ 2026-07-21

### 博客搭建
- Hexo 7.3.0 + Butterfly 5.5.5
- GitHub Pages 部署（source 分支 → main 分支）
- 坚果云同步文章（Junction 链接 `source/_posts` → 坚果云 `Blog/_posts`）
- GitHub Actions 自动部署

### 文章
- 鲁迅先生的冷与热
- 关于
- 【补完计划】《鼠疫》与《局外人》
- 我看娜拉出走
- 【补完计划】俗女养成记

### 功能
- 本地搜索（local_search）
- 不蒜子 → Vercount 统计
- PJAX 无刷新切换
- 鼠标拖尾特效（Canvas）
- Bing 站长验证
