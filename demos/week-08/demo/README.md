# Jekyll 演示示例

本目录包含 Web/Jekyll 课程的完整演示代码。

## 示例列表

| 示例 | 名称 | 说明 |
|------|------|------|
| 01 | 简单网站 | 基础 Jekyll 站点结构 |
| 02 | 自定义主题 | 自定义布局和 Liquid 模板 |

## 前置知识

- Markdown 基础语法
- HTML/CSS 基础（可选，用于自定义主题）

## 快速开始（GitHub Pages）

1. 将任意示例目录的内容推送到 GitHub 仓库
2. 进入仓库 → Settings → Pages
3. Source 选择 "Deploy from a branch"
4. Branch 选择 `main` 或 `gh-pages`，文件夹选择 `/ (root)`
5. 点击 Save
6. 等待几分钟，网站就会上线！

## Jekyll 核心概念

### 1. Front Matter

每个页面/文章开头的 YAML 配置：

```yaml
---
layout: post
title: "文章标题"
date: 2026-03-16 10:00:00 +0800
categories: 分类
---
```

### 2. 目录结构

```
_site/              # 生成的静态网站（自动生成）
_layouts/           # 布局模板
_posts/             # 博客文章（YYYY-MM-DD-title.md）
_includes/          # 可复用的代码片段
_data/              # 数据文件（YAML/JSON/CSV）
assets/             # CSS/JS/图片等静态资源
_config.yml         # 全局配置
index.md            # 首页
```

### 3. 命名约定

- 文章文件：`YYYY-MM-DD-title.md`
- 布局文件：`_layouts/xxx.html`
- 包含文件：`_includes/xxx.html`

## Markdown 快速参考

```markdown
# 一级标题
## 二级标题

**粗体**  *斜体*  `代码`

- 无序列表
- 项目二

1. 有序列表
2. 第二步

[链接](https://example.com)
![图片](image.jpg)

```代码块
print("Hello")
```

> 引用文字
```

## 常用资源

- [Jekyll 官方文档](https://jekyllrb.com/docs/)
- [Markdown 指南](https://www.markdownguide.org/)
- [GitHub Pages 文档](https://pages.github.com/)
