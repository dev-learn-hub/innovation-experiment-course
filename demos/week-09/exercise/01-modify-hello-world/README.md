# 练习 1：修改 Hello World

## 任务

1. 进入 `demo/01-hello-world` 目录
2. 修改 `lib/main.dart` 中的文本内容
3. 改变文本的样式（颜色、大小、字体）
4. 改变 AppBar 的颜色

## 要求

- [ ] 文本已修改为你的名字或学号
- [ ] 文本大小已改变
- [ ] 文本颜色已改变
- [ ] AppBar 颜色已改变
- [ ] 应用能正常运行

## 提示

```dart
// 修改文本
Text(
  '你的名字',
  style: TextStyle(
    fontSize: 48,           // 字体大小
    color: Colors.red,      // 颜色
    fontWeight: FontWeight.bold,  // 粗体
  ),
)

// 修改 AppBar 颜色
AppBar(
  backgroundColor: Colors.green,
  title: const Text('我的应用'),
)
```

## 验收

运行应用后，确认：
- 文本已更新
- 样式已改变
- 应用无错误
