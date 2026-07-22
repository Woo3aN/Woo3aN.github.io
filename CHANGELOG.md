# 博客更新日志

## 2026-07-22

### 界面调整
- 菜单「关于」→「About」
- 搜索按钮「搜索」→「Search」；弹窗标题 + 输入框保留中文
- Archives 大标题「Archives」→「归档」，与 Tags「标签」/ Categories「分类」统一
- 归档页按月分组（2026 → 2026年07月）
- 归档月标题时间线与年份对齐

### 统计
- Vercount `site_pv` 每天重置：确认是 Vercount 后端 bug
- GitHub Actions 移除 `hexo clean`，减少触发数据重置

### 搜索
- 配置 Bing Webmaster Tools 并验证成功
- 百度站长平台：github.io 域名名额已满，需自定义域名

### SEO
- `robots.txt` 声明 Google + Baidu sitemap
- `_config.yml` 补充 `description` 和 `keywords`

### 日期
- 文章 frontmatter 日期统一加时间戳，避免跨时区偏移
- Actions 智能 mtime：文章内容未变不刷新更新日期

### PJAX
- 关闭 PJAX（与 Vercount 有兼容问题，待修复）

---

## 2026-07-21

### Vercount 迁移
- 不蒜子 → Vercount（`events.vercount.one/js`）
- `site_pv` 每天重置，调试多日确认是 Vercount 后端问题

### 部署优化
- Node.js 20 → 22
- `fetch-depth: 0`，git 历史恢复文件 mtime
- `hexo clean` 还原为仅 `generate`
- 文章内容 diff 检测，避免改配置刷新日期

---

## 2026-07-20

### SEO & 验证
- 添加 `robots.txt`
- Bing 站长平台 HTML Meta Tag 验证

---

## 2026-07-19

### 发布文章
- 【补完计划】俗女养成记
- 我看娜拉出走

---

## 2026-07-16

### 文章
- 发布【补完计划】《鼠疫》与《局外人》
- 加缪文章添加图片

---

## 2026-07-15

### 博客搭建
- Hexo 7.3.0 + Butterfly 5.5.5 主题
- GitHub Pages（source 分支 → main 分支部署）
- 坚果云同步文章（Junction: `source/_posts` → `D:\我的坚果云\Blog\_posts`）
- GitHub Actions 自动部署

### 文章
- 鲁迅先生的冷与热
- 关于（About 页面）

---

## 2026-07-14 及之前

### 主题切换与配置
- Fluid 主题 → Butterfly 主题
- 配置：自动暗色模式、本地搜索、封面图、头像、favicon
- Blue-Purple 蓝紫配色方案
- Giscus 评论系统（Fluid 时期）
- 不蒜子统计（后来换 Vercount）
- 粒子网络背景 + 鼠标拖尾特效（后来关闭）
- PJAX 无刷新切换（后来关闭）
- 分类和标签页面配置
- 时区修复（Asia/Shanghai）
- Sticky 置顶排序
