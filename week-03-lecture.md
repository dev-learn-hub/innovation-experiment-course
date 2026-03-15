# 第3周讲义：Robocode 机器人对战

---

## 一、Robocode 平台简介

### 1.1 什么是 Robocode？
Robocode 是一个基于 Java 的编程游戏，玩家通过编写 Java 代码来控制坦克机器人在战场上进行对战。

### 1.2 Robocode 的特点
- 实时对战：机器人在真实时间中移动和战斗
- 完整的物理引擎：碰撞、弹道、能量管理
- 事件驱动编程：通过事件响应战场变化
- 丰富的 API：移动、扫描、射击、雷达等

---

## 二、环境搭建

### 2.1 安装 Robocode
1. 下载 Robocode：https://robocode.sourceforge.io/
2. 解压到本地目录
3. 运行 `robocode.bat`（Windows）或 `robocode.sh`（Linux/Mac）

### 2.2 配置开发环境
#### Eclipse 配置：
1. 创建 Java 项目
2. 添加 Robocode 的 `libs/robocode.jar` 到 classpath
3. 配置输出目录为 Robocode 的 `robots` 目录

#### IntelliJ IDEA 配置：
1. 创建 Java 项目
2. 在 Project Structure 中添加 `robocode.jar` 作为库
3. 配置编译输出路径

---

## 三、机器人基础

### 3.1 机器人结构
```java
public class MyRobot extends Robot {
    public void run() {
        // 机器人主循环
        while (true) {
            ahead(100);
            turnGunRight(360);
        }
    }
    
    public void onScannedRobot(ScannedRobotEvent e) {
        // 扫描到敌人时触发
        fire(1);
    }
}
```

### 3.2 核心方法
- `ahead(double distance)` - 向前移动
- `back(double distance)` - 向后移动
- `turnLeft(double degrees)` - 左转
- `turnRight(double degrees)` - 右转
- `turnGunLeft(double degrees)` - 炮管左转
- `turnGunRight(double degrees)` - 炮管右转
- `fire(double power)` - 开火

### 3.3 事件处理
- `onScannedRobot(ScannedRobotEvent e)` - 扫描到敌人
- `onHitByBullet(HitByBulletEvent e)` - 被子弹击中
- `onHitRobot(HitRobotEvent e)` - 撞到敌人
- `onHitWall(HitWallEvent e)` - 撞到墙壁

---

## 四、第一个机器人：HelloWorld

### 4.1 代码示例
```java
import robocode.*;

public class HelloWorld extends Robot {
    public void run() {
        while (true) {
            ahead(100);
            turnRight(90);
        }
    }
    
    public void onScannedRobot(ScannedRobotEvent e) {
        fire(1);
    }
}
```

### 4.2 测试机器人
1. 编译机器人
2. 启动 Robocode
3. 创建新对战
4. 选择 HelloWorld 和示例机器人
5. 开始对战！

---

## 五、简单对战策略

### 5.1 移动策略
- 不停移动，避免成为靶子
- 保持距离，避免近战
- 不规则移动，难以预测

### 5.2 射击策略
- 扫描到敌人立即射击
- 根据距离调整火力
- 预测敌人移动方向

### 5.3 进阶：线性预测
```java
public void onScannedRobot(ScannedRobotEvent e) {
    double absoluteBearing = getHeading() + e.getBearing();
    double bearingFromGun = normalRelativeAngle(absoluteBearing - getGunHeading());
    
    if (Math.abs(bearingFromGun) <= 3) {
        turnGunRight(bearingFromGun);
        fire(2);
    } else {
        turnGunRight(bearingFromGun);
    }
}
```

---

## 六、课后练习

1. 修改 HelloWorld 机器人，让它在移动时同时旋转炮管
2. 实现一个机器人，当扫描到敌人时停止移动并射击
3. 设计一个简单的躲避策略，当被子弹击中时改变方向

---

## 七、拓展阅读
- [Robocode Wiki - Getting Started](https://robowiki.net/wiki/Robocode_Basics)
- [Robocode API 文档](https://robocode.sourceforge.io/docs/robocode/)
