<!--
 * @Author: 66lueflam144 117815219+66lueflam144@users.noreply.github.com
 * @Date: 2022-11-09 17:48:23
 * @LastEditors: 66lueflam144 117815219+66lueflam144@users.noreply.github.com
 * @LastEditTime: 2022-11-10 09:50:02
 * @FilePath: \web.ufod:\GitHub\blueflame\Tasks111\web.ufo\learn-HTML.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
___Hyper Text Markup Language___
`HTML是一种标记语言`:astonished:
# HTML基础 :innocent:
- 元素(__标签只是它的一部分__)
  - 元素构造：`<开始标签>+<内容>+<结束标签>`
  - 嵌套元素：`<元素1><元素2>+<内容>+</元素2></元素1>`
  - 块级元素：*该元素以块的形式展现，常用于页面结构化内容，如段落、列表、导航菜单、页脚。*
  - 内联元素：*在块级元素中并环绕文档内容的一小部分，而不是一整个段落或者一组内容。内联元素不会导致文本换行：它通常出现在一堆文字之间。* 
  - 空元素：*不是所有元素都拥有开始标签，内容，结束标签。一些元素只有一个标签，通常用来在此元素所在位置插入/嵌入一些东西。*
- 内容
    - 主内容类：
      - 元数据内容，如`<base>,<link>,<title>`
      - 流式内容：比较广泛，包括`标题元素，分段元素，措辞元素、嵌入元素、互动元素和表单相关元素。它还包括文本节点（但不包括那些只由空白字符组成的节点）`<br>如`<aside>,<code>,<hi>,<p>,<sub>...`
        - 分段内容
        - 标题内容
        - 短语内容（纯文本不完全是空字符也属于该内容）
        - 嵌入内容：如`<img>,<svg>,<audio>`
        - 交互内容，如`<button>,<label>`
    - 表单相关内容，如`<form>,<fieldest>,<lable>`
    - 特殊内容
- 属性 :属性包含元素额外信息（invisual)。 
  - 属性内容：<br>*1.一个空格，在属性和元素名称之间（如果已经有一个或多个属性，就与前一个属性之间有一个空格）。<br>2.属性名称，后面跟着一个等于号。<br>3.一个属性值，由一对引号 ("") 引起来。*
  - 布尔属性：没有值的合法的属性。只有与之属性名一样的属性值。
  - 附：多个属性内容时should be like this example-`<a href="https://xxxx" title="funxxx"><内容></a>`

*<a href="https://www.runoob.com/tags/ref-standardattributes.html" title="HTML标准属性参考">HTML标准属性参考</a>*<br>
*<a href="https://www.runoob.com/tags/html-reference.html">HTML标签参考</a>*
****
## HTML实体字符引用 :innocent:
| 原义字符 |HTML实体名称|
|---|---|
| > |`&gt;`|
| < |`&lt;`|
| " |`&quot;`|
| ' |`&apos;`|
| & |`&amp;`|
|  |`&nbsp;`|

*列举了一些常用的:<a href="https://www.runoob.com/tags/ref-entities.html" title="the whole tags">the whole tags</a>*
***
## HTML注释 :innocent:
`<!-- <p>xxx</p> -->`
***
## HTML 标题 :innocent:
`<h1>xx</h1>`
从1到6逐渐减小标题大小。

## HTML链接
种语法：

`<a href="url">link text</a>`normal版

`<a href="URL">xxx</a>`（xxx为链接外貌）

title属性：`<a href="URL" title="xxx">yyy</a>`（光标显示title）

target 属性：`<a href="URL" target="zzz">xxx</a>`<i>（定义被链接的文档在何处显示）</i>

name属性：`<a name="label">xxx</a>`(使用 name 属性创建 HTML 页面中的书签。)
使用示例
>`<a name="xxx">y-z</a>`(对锚命名/创建书签)
`<a href="#xxx">z</a>`(文档内创建指向该锚的链接)&nbsp;&nbsp;//<br>`<a href="URL#xxx">z</a>`(其他页面指向该锚的链接)

<b>"链接文本" 不必一定是文本。图片或其他 HTML 元素都可以成为链接。</b>

## HTML图片

### 定义图像语法
`<img src="URL" />`
- <b>背景图片</b>：<br>`<body background="URL">`git和jpg图片可作为HTML背景，当图片小于页面的时候，图片会进行重复。
- <b>排列图片</b>：<br>(1)普适版：`xxx<img src="URL">xxx`<br>(2)进阶版对齐方式：`<img src="URL" align="bottom/middle/top">`<br>bottom是默认对齐方式。
- <b>浮动图像</b>：<br>`<img src="URL（gif）" align="left/right">`图像浮动在文档左/右两侧。
- <b>调整图像大小</b>：<br>`<img src="URL" width="x" height="y">`
- <b>图像链接</b>：<br>`<a href="URL">`<br>`<img border="0" src="URL" />`<br>`</a>`<br>将图片作为链接使用。
- 创建图像映射：<img src="">


## HTML表格和列表
my god