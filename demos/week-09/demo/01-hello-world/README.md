# 示例 1：Hello World

这是最基础的 Flutter 应用示例。

## 快速开始

```bash
cd demos/week-09/demo/01-hello-world
flutter run
```

## 核心概念

### 1. StatelessWidget

无状态的组件，不会改变。

```dart
class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(...);
  }
}
```

### 2. Scaffold

提供基本的 Material Design 布局。

```dart
Scaffold(
  appBar: AppBar(...),      // 顶部导航栏
  body: Center(...),        // 主体内容
)
```

### 3. 常用 Widget

| Widget | 作用 |
|--------|------|
| `MaterialApp` | 应用根组件 |
| `Scaffold` | 页面脚手架 |
| `AppBar` | 顶部导航栏 |
| `Center` | 居中布局 |
| `Text` | 文本显示 |

## 功能

- 显示应用标题
- 在页面中央显示 "Hello, Flutter!"

## 学习要点

1. 理解 Widget 树的概念
2. 掌握基本的 Material Design 组件
3. 理解 build 方法的作用
4. 学会使用 Text 和 Center 组件
