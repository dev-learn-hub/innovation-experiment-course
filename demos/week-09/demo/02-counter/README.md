# 示例 2：计数器应用

这是一个展示 StatefulWidget 和状态管理的示例。

## 快速开始

```bash
cd demos/week-09/demo/02-counter
flutter run
```

## 核心概念

### 1. StatefulWidget

有状态的组件，可以改变内部状态。

```dart
class CounterPage extends StatefulWidget {
  @override
  State<CounterPage> createState() => _CounterPageState();
}
```

### 2. State 类

管理 StatefulWidget 的状态。

```dart
class _CounterPageState extends State<CounterPage> {
  int _counter = 0;
  
  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }
}
```

### 3. setState

更新状态并重新构建 UI。

```dart
setState(() {
  _counter++;  // 修改状态
});  // 触发重新构建
```

## 功能

- 点击 + 按钮增加计数
- 点击 - 按钮减少计数
- 实时显示计数值

## 学习要点

1. 理解 StatefulWidget 和 State 的关系
2. 掌握 setState 的使用
3. 理解 Widget 重建的时机
4. 学会使用 FloatingActionButton
5. 学会使用 Row 进行水平布局
