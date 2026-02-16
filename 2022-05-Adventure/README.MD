# 2D Game Framework Prototype (Python & Pyglet)

## 项目简介 / Project Overview
本项目是一个基于 Python 和 Pyglet 库开发的 2D 游戏开发框架。项目初衷是探索游戏引擎的底层逻辑，包括自定义碰撞检测算法、对象生命周期管理以及复杂的坐标变换系统。该框架支持多对象协同处理、多种输入模式（键盘+鼠标）以及动态图像资源管理。

This project is a 2D game development framework built with Python and Pyglet. It was developed to explore the underlying logic of game engines, including custom collision detection algorithms, object lifecycle management, and complex coordinate transformation systems. The framework supports collaborative multi-object handling, multiple input modes (Keyboard + Mouse), and dynamic sprite resource management.

---

## 技术亮点 / Technical Highlights

### 1. 自定义数学与几何逻辑 / Custom Mathematical & Geometric Logic
不同于直接调用物理引擎，本项目手动实现了基础的向量运算和几何判定逻辑：
*   **坐标旋转算法 (Rotation Logic):** 基于三角函数实现了点绕中心点旋转的计算。
*   **角度判定 (Angle Calculation):** 实现了物体间夹角计算，用于实现“追踪”和“面向鼠标”等行为。
*   **自定义碰撞检测 (Custom Collision Detection):** 使用了射线判定/点在多边形内的逻辑 (`block_in`, `dot_for_line`)，支持非轴齐平 (Non-AABB) 的旋转碰撞盒。

Instead of relying on high-level physics engines, I manually implemented fundamental vector operations and geometric logic:
*   **Coordinate Rotation:** Implemented point-around-center rotation based on trigonometric functions.
*   **Angle Predication:** Calculated relative angles between objects to enable "Homig" and "Look-at-Mouse" behaviors.
*   **Collision Detection:** Implemented custom intersection logic (`block_in`, `dot_for_line`) supporting oriented bounding boxes (OBB) and point-in-polygon tests.

### 2. 面向对象的设计模式 / Object-Oriented Architecture
项目采用了深度的继承结构，提高了代码的可复用性：
*   **`Object` Class:** 封装了位置、旋转、缩放、碰撞盒更新等核心属性。
*   **`Player` Class:** 继承自 `Object`，集成了四种不同的移动控制逻辑（例如：相对方向移动、鼠标指向移动），展示了对输入控制流的灵活处理。
*   **`Team` Class (Lifecycle Management):** 实现了一个容器类，用于统一管理对象的绘制、状态更新及自动内存保护（处理对象死亡与清理）。

The project utilizes a deep inheritance structure to enhance code reusability:
*   **`Object` Class:** Encapsulates core attributes like position, rotation, scaling, and bounding box updates.
*   **`Player` Class:** Inherits from `Object`, integrating four distinct movement control schemes (e.g., relative movement, mouse-aiming movement).
*   **`Team` Class (Lifecycle Management):** A container class designed for batch rendering, state updates, and automated memory protection (handling object disposal).

### 3. AI 状态机原型 / AI & State Management
每个对象内置了 `AI` 类（即 `ias` 模块），用于跟踪实体的生理状态（生命值、护甲）及行为状态（是否正在移动、旋转），为后续开发复杂的非玩家角色行为树提供了基础。

Each object contains an internal `AI` class instance (`ias`), used to track physical stats (HP, Armor) and behavioral states (is_moving, is_rotating), providing a foundation for future implementation of NPC behavior trees.

---

## 技术栈 / Tech Stack
*   **Language:** Python 3.x
*   **Graphics Library:** Pyglet (OpenGL wrapper)
*   **Image Processing:** Pillow (PIL), NumPy
*   **Algorithms:** Linear Algebra, Trigonometry, Collision Detection

---

## 如何运行 / How to Run
1.  确保已安装依赖 / Ensure dependencies are installed:
    ```bash
    pip install pyglet pillow numpy
    ```
2.  运行主程序 / Run the main script:
    ```bash
    python main.py
    ```

---

## 开发者说明 / Developer's Note
该项目展示了我对底层数学逻辑如何转化为视觉交互的理解。在大学院的研究中，我希望进一步探索高性能碰撞检测及复杂场景下的路径规划算法。

This project demonstrates my understanding of translating low-level mathematical logic into visual interaction. In my future graduate studies, I aim to further explore high-performance collision detection and pathfinding algorithms in complex environments.
