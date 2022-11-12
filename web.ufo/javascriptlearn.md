
# JavaScript


`JavaScript 是互联网上最流行的脚本语言，这门语言可用于 HTML 和 web，更可广泛用于服务器、PC、笔记本电脑、平板电脑和智能手机等设备。JavaScript 是一种轻量级的编程语言。`

`JavaScript 是可插入 HTML 页面的编程代码。`

`JavaScript 插入 HTML 页面后，可由所有的现代浏览器执行。`

`JavaScript 与 Java 是两种完全不同的语言，无论在概念上还是设计上。`

____
## JavaScript使用
JavaScript脚本代码放置于`<script>` `</script>`之间
但外部脚本（.js）中不能包含`<script>`标签。

___
### HTML内使用JavaScript
>可以在 HTML 文档中放入不限数量的脚本。

>脚本可位于 HTML 的 <body> 或 <head> 部分中，或者同时存在于两个部分中。

>通常的做法是把函数放入 <head> 部分中，或者放在页面底部。这样就可以把它们安置到同一处位置，不会干扰页面的内容。

### 使用外部JavaScript

>`<script src="xxxx.js></script>`

### JavaScript输出

|类别|作用|
|---|---|
|window.alert()|弹出警告窗|
|document.write()|将内容写入HTML文档中|
|innerHTML|写入HTML元素中|
|console.log()|写入浏览器控制台|

#### windows.alert(xxx)
xxxx就是内容，打开网页时弹窗显示警告xxx。

#### document.write()
仅仅输出文档，如果文档加载后执行document.write()整个HTML页面会被覆盖。（类似切换了界面）

#### innerHTML
如：<br>`document.getElementByID("xxx").innerHTML="yyy"`<br>
向标识为xxx的HTML元素插入yyy。

#### console.log()
<a href=https://www.runoob.com/js/js-output.html>请往这看</a>

___
### JavaScript语法


>每个语句以`;`结束，语句块使用`{ }`,不建议一行多语句。
请注意，JavaScript严格区分大小写，如果弄错了大小写，程序将报错或者运行不正常。

- 赋值语句：`var y=xxx;`
可以是=1；也可以是=1+3；
- 字符串但仍视为语句`'xxx';`

### 数据类型
(数据家族的故事连载于<a href=https://www.liaoxuefeng.com/wiki/1022910821149312/1023020925712064>&hearts;click to know more details</a>)

- Number
- 字符串(字符串豪门家族的故事请看<a href=https://www.liaoxuefeng.com/wiki/1022910821149312/1023020952022784>&spades;click to know more about `\`</a>)
- 布尔值
- 比较运算符
- null和undefined
- 数组 &nbsp;&clubs;<a href=https://www.liaoxuefeng.com/wiki/1022910821149312/1023020967732032>more details</a>
- 对象
- 变量





