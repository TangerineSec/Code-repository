太好了！JS 语法 + DOM 操作是前端开发的核心之一。以下是一个 **30 分钟的高效学习计划**，适合初学者巩固 JavaScript 基础 + 动手练习 DOM 操作。

---

## 🧠 学习目标（30 分钟内）

1. 掌握 JS 变量、函数、事件基础语法。
2. 掌握 DOM 结构基本理解。
3. 使用 JS 操作页面元素（读写文本、改样式、监听事件）。
4. 完成一个小测验 + 练习项目。

---

## 🕒 时间分配（30 分钟）

| 时间段        | 内容                  |
| ---------- | ------------------- |
| 0 - 10 分钟  | JS 基础语法精讲（变量、函数、事件） |
| 10 - 20 分钟 | DOM 操作讲解 + 实战演示     |
| 20 - 30 分钟 | 小测验 + 编码练习          |

---

## 📚 0 - 10 分钟：JS 基础语法精讲

### 🔹 变量声明

```js
let name = 'Master';
const age = 30;
var mood = 'happy';  // 不推荐，了解即可
```

### 🔹 函数定义

```js
function greet(person) {
  return `Hello, ${person}`;
}
```

### 🔹 简单事件监听

```js
document.getElementById("btn").addEventListener("click", function() {
  alert("你点击了按钮！");
});
```

✅ **教学方法：用“说-写-试”循环学习**

* **说**：用自然语言描述你想做的事情
* **写**：写出代码
* **试**：立即在浏览器中尝试

---

## 📘 10 - 20 分钟：DOM 操作讲解 + 实战演示

### DOM 结构示意：

HTML

```html
<p id="demo">原始文字</p>
<button id="changeText">点我修改文字</button>
```

### JS 操作

```js
const p = document.getElementById("demo");
const btn = document.getElementById("changeText");

btn.addEventListener("click", function() {
  p.innerText = "你好，世界！";
  p.style.color = "red";
});
```

### 常见操作总结：

| 操作   | 方法                                              |
| ---- | ----------------------------------------------- |
| 获取元素 | `document.getElementById()` / `querySelector()` |
| 修改文字 | `element.innerText = ...`                       |
| 修改样式 | `element.style.color = ...`                     |
| 添加事件 | `element.addEventListener()`                    |

✅ **教学方法：类比现实生活**

* 你是导演（JS）
* 网页是舞台（DOM）
* 元素是演员（HTML 标签）
* 你让“演员说台词”（修改文本）、“换衣服”（改样式）、“走位跳舞”（添加动画）

---

## ✍️ 20 - 30 分钟：小测验 + 编码练习

### ✅ 小测验（做对了继续，做错了解释）

**Q1:** 下列哪个方法可以获取元素？

```js
A. document.find("myId")
B. document.getElementById("myId")
C. window.getElement("myId")
```

**Q2:** 如何让一个按钮被点击时改变段落文字内容？

```js
A. button.innerText("新内容")
B. p.addEventListener("click")
C. button.addEventListener("click", ()=> { p.innerText = "新内容" })
```

答案：B、C

---

### 🧪 编码练习任务：实现一个“点击按钮改变背景颜色”的功能

HTML：

```html
<button id="bgBtn">切换背景色</button>
```

JS：

```js
const btn = document.getElementById("bgBtn");

btn.addEventListener("click", function() {
  document.body.style.backgroundColor = 
    document.body.style.backgroundColor === "lightblue" ? "white" : "lightblue";
});
```

---

## 🔁 学习建议总结

| 技巧      | 描述                       |
| ------- | ------------------------ |
| F12 是朋友 | 使用浏览器开发者工具调试             |
| 实战优先    | 每学一个点都**立即尝试写代码**        |
| 多改多点    | 鼓励多点几次、改一改，观察页面反应        |
| 小而频繁    | 每天学 20\~30 分钟，比一次熬夜猛学更有效 |

---

如果你需要我为这个内容生成 HTML + JS 可运行的小页面模板，或者制作“记忆卡片”版本，随时说一声！或者我们继续下一阶段的学习目标也可以，例如：

* 动态创建元素
* 表单处理
* 本地存储（localStorage）

继续学习，我们轻松做一个会动的网页导演 😎🎬
