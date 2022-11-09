*`cascading style sheets`*
# __CSS__ 
>*__释义一__*：一种用来为结构化文档（HTML文档或XML应用）添加样式的计算机语言，其文件扩展名为`.css`。<br>
>*__释义二__*：将样式信息与网页内容分离的一种语言，为每个元素定义样式，主要用于美化HTML页面。

ps:HTML标签构成了网页的基本结构，只是一个框架，CSS就是来装修的。
## __CSS作用__
>通过设置对应的css样式属性可以修改HTML文档内各元素的显示，位置等样式。

## __CSS语法__

CSS rule-set由**选择器**和**声明块**组成。
|类别|功能|
|---|---|
|选择器|指向需要设置样式的HTML元素|
|声明块|包含一条或多条用分号间隔的声明|
|声明|包含一个CSS属性名称和一个值（一冒号分隔）|


`多条CSS声明用分号分隔，声明块使用花括号括起来`
>example
__p__ &nbsp; &nbsp;//选择器，指向要设置是元素，这里指`<p>`<br>
{
    __color:red;__&nbsp;&nbsp;//声明。这条是第一条声明，`color`是属性，`red`是属性值<br>
    <b>text-align:center;</b>&nbsp;&nbsp;//第二条声明，`text-align`是属性，`center`是属性值。<br>
}
这一个为声明块。

### CSS选择器
<br>
CSS选择器分类：<br>
- <a href=https://www.w3school.com.cn/css/css_selectors.asp>简单选择器</a>(包括<i>CSS元素选择器，CSS id选择器，CSS类选择器，CSS通用选择器，CSS分组选择器</i>)<br>
- <a href=https://www.w3school.com.cn/css/css_combinators.asp>组合器选择器</a><br>
- <a href=https://www.w3school.com.cn/css/css_pseudo_classes.asp>伪类选择器</a><br>
- <a href=https://www.w3school.com.cn/css/css_attribute_selectors.asp> 属性选择器</a><br>
- <a href=https://www.w3school.com.cn/css/css_pseudo_elements.asp>伪元素选择器</a><br>

#### CSS元素选择器
`根据元素名称来选择HTML元素`如上面例子中的`<p>`

#### CSS id选择器
`id 选择器使用 HTML 元素的 id 属性来选择特定元素。`
`元素的 id 在页面中是唯一的，因此 id 选择器用于选择一个唯一的元素！`
`要选择具有特定 id 的元素，请写一个井号（＃），后跟该元素的 id。(id 名称不能以数字开头)`
>#test<br>
{
    text-align:center;
    color:red;
}
这条CSS规则将运用于id=“test”的HTML元素

#### CSS类选择器


