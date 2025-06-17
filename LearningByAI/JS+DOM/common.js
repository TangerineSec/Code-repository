// 变量声明
let name = 'Master';
const age = 18;
var mood = 'happy';

// 函数定义
function greet(person){
    return `Hello,${person}`;
}

//  事件监听
document.getElementById('btn').addEventListener
('click',function(){
    alert("按钮点击");
})

// DOM 操作：
<p id="demo">原始文字</p>
<button id="ChangeText">点击修改文字</button>

const p  = document.getElementById('demo');
const btn = document.getElementById('ChangeText');
btn.addEventListener('click',function(){
    p.innerText = '你好，世界！';
    p.style.color = 'red';
});

// 编码练习任务：实现一个点击按钮改变背景颜色的功能
```html
<button id="bgBtn">点击切换背景色</button>
```
```js
const button-document=document.getElementById('bgBtn');
button-document.addEventListener('click),funtion(){
    document.boby.style.backgroupColor='pink';
}
```