# 示例 1：简单的 Jekyll 网站

这是一个最基础的 Jekyll 网站示例。

## 文件结构

```
01-simple-site/
├── _config.yml          # 配置文件
├── index.md            # 首页
├── about.md            # 关于页面
└── _posts/             # 文章目录
    ├── 2026-03-16-first-post.md
    └── 2026-03-17-markdown-demo.md
```

## 核心概念

### 1. Front Matter

每个 Markdown 文件开头的 YAML 格式配置：

```yaml
---
layout: post
title: "文章标题"
date: 2026-03-16 10:00:00 +0800
categories: 分类
---
```

### 2. _config.yml

网站的全局配置文件：

```yaml
title: 网站标题
description: 网站描述
theme: minima
```

### 3. _posts 目录

存放博客文章，文件名格式：`YYYY-MM-DD-title.md`

## 在 GitHub Pages 上使用

1. 将此目录内容推送到 GitHub 仓库
2. 在仓库设置中开启 GitHub Pages
3. 选择 main 分支作为源
4. 几分钟后网站就会上线！
