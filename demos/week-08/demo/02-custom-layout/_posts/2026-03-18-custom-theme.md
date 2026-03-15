---
layout: post
title: "如何创建自定义 Jekyll 主题"
date: 2026-03-18 09:00:00 +0800
categories: 教程
---

# 创建自定义 Jekyll 主题

Jekyll 允许你创建完全自定义的主题和布局。

## 步骤

### 1. 创建 _layouts 目录

```
_layouts/
├── default.html    # 默认布局
└── post.html       # 文章布局
```

### 2. 使用 Liquid 模板语法

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ page.title }}</title>
</head>
<body>
    {{ content }}
</body>
</html>
```

### 3. 在 Front Matter 中指定布局

```yaml
---
layout: post
title: "文章标题"
---
```

## 常用 Liquid 标签

| 标签 | 说明 |
|------|------|
| `{{ site.title }}` | 网站标题 |
| `{{ page.title }}` | 页面标题 |
| `{{ content }}` | 页面内容 |
| `{% for post in site.posts %}` | 遍历文章 |
| `{{ post.url }}` | 文章 URL |
| `{{ post.date | date: '%Y-%m-%d' }}` | 格式化日期 |

希望这篇教程对你有帮助！
