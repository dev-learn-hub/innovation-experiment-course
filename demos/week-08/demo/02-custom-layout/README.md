# 示例 2：自定义布局和主题

这个示例展示如何创建自定义的 Jekyll 布局和主题。

## 文件结构

```
02-custom-layout/
├── _config.yml
├── index.md
├── _layouts/
│   ├── default.html    # 默认布局
│   └── post.html       # 文章布局
└── _posts/
    └── 2026-03-18-custom-theme.md
```

## 布局继承

- `default.html` - 基础布局，包含页头、导航、页脚
- `post.html` - 继承 default，添加文章特有的元素

## Liquid 语法要点

### 变量

```liquid
{{ site.title }}    <!-- 网站配置中的 title -->
{{ page.title }}    <!-- 当前页面的 title -->
{{ content }}       <!-- 当前页面的内容 -->
```

### 循环

```liquid
{% for post in site.posts %}
  <a href="{{ post.url }}">{{ post.title }}</a>
{% endfor %}
```

### 过滤器

```liquid
{{ post.date | date: '%Y-%m-%d' }}
{{ page.title | upcase }}
```

## 进一步学习

- [Jekyll 模板文档](https://jekyllrb.com/docs/templates/)
- [Liquid 语法](https://shopify.github.io/liquid/)
