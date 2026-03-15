---
layout: default
title: 首页
---

# 欢迎来到自定义主题网站！

这是一个使用自定义布局的 Jekyll 网站示例。

## 最新文章

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <small>{{ post.date | date: '%Y-%m-%d' }}</small>
    </li>
  {% endfor %}
</ul>
