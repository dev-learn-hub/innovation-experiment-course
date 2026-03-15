# 练习 2：创建计数器

## 任务

1. 创建一个新的 Flutter 项目：`flutter create my_counter`
2. 参考 `demo/02-counter` 的代码
3. 实现一个计数器应用
4. 添加自己的功能（如重置按钮）

## 要求

- [ ] 项目能成功创建
- [ ] 能显示计数值
- [ ] + 按钮能增加计数
- [ ] - 按钮能减少计数
- [ ] 应用能正常运行

## 提示

### 创建项目

```bash
flutter create my_counter
cd my_counter
```

### 基本结构

```dart
class _CounterPageState extends State<CounterPage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('计数器')),
      body: Center(
        child: Text('$_counter', style: const TextStyle(fontSize: 48)),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        child: const Icon(Icons.add),
      ),
    );
  }
}
```

## 拓展功能（可选）

- 添加减少按钮
- 添加重置按钮
- 改变按钮样式
- 添加背景颜色

## 验收

运行应用后，确认：
- 计数器能正常工作
- 按钮能响应点击
- 应用无错误
