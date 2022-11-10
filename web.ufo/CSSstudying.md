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
  
  ___
#### CSS元素选择器
`根据元素名称来选择HTML元素`如上面例子中的`<p>`
____
#### CSS id选择器`#`
`id 选择器使用 HTML 元素的 id 属性来选择特定元素。`
`元素的 id 在页面中是唯一的，因此 id 选择器用于选择一个唯一的元素！`
`要选择具有特定 id 的元素，请写一个井号（＃），后跟该元素的 id。`

id 名称不能以数字开头
>#test<br>
{
    text-align:center;
    color:red;
}
这条CSS规则将运用于id=“test”的HTML元素
____
#### CSS类选择器`.`
`该选择器选择有特定class属性的HTML元素。`
`需选择拥有特定 class 的元素，请写一个句点（.）字符，后面跟类名。`
>.center&nbsp;&nbsp;(所有带有class="center"的HTML元素变成红色)//&nbsp;p.center（所有带有class="center"的`<p>`元素变成红色)
{
    text-align:center;
    color:red;
}


附：引用多个类
>`<p class="center large">xxx</p>`这表示该段落引用了center和large两个类。

类名不能以数字开头。
____
#### CSS通用选择器`*`

`该选择器平等地影响页面上所有HTML元素`
example:
>*{
    text-align:center;
    color:blue;
}

____
#### CSS分组选择器`,`
`分组选择器选取所有具有相同样式定义的 HTML 元素`
如，对`h1`,`p`,合并写成:
>h1,p{<br>
    text-aligggn:center;<br>
    color:red;<br>
}


### CSS设置元素基础样式

#### CSS颜色

---
1.背景颜色`<p style="background-color:Yellow;">背景颜色</p>`<br>
效果如下：<br>
<p style="background-color:Yellow;">背景颜色</p>
<br><b><a href="https://www.w3school.com.cn/css/css_background.asp">CSS背景颜色设置</a></b>

---
2.文本颜色`<p style="color:Tomato;">文本颜色</p>`<br>
效果如下：<br>
<p style="color:Tomato;">文本颜色</p>

----
3.边框颜色`<h1 style="border:2px solid red;">边框颜色</h1>`<br>
效果如下：<br>
<h1 style="border:2px solid red;">边框颜色</h1>

___
#### CSS颜色值
>在 CSS 中，可以使用 RGB 值、HEX 值、HSL 值、RGBA 值或者 HSLA 值来指定颜色

- <a href="https://www.w3school.com.cn/css/css_colors_rgb.asp">RGB颜色</a>
- <a href="https://www.w3school.com.cn/css/css_colors_hex.asp">HEX颜色</a>
- <a href="https://www.w3school.com.cn/css/css_colors_hsl.asp">HSL颜色</a>

#### CSS背景

- <b><a href="https://www.w3school.com.cn/css/css_background.asp">CSS背景颜色设置</a>
- <a href="https://www.w3school.com.cn/css/css_background_image.asp">背景图像设置</a>
- <a href="https://www.w3school.com.cn/css/css_background_repeat.asp">背景重复</a>
- <b><a href="https://www.w3school.com.cn/css/css_background_attachment.asp"></b>背景附着</a>指定背景图像是应该滚动还是固定的（不会随页面的其余部分一起滚动）
- <b><a href="https://www.w3school.com.cn/css/css_background_shorthand.asp">背景属性简写</a></b>
___
#### CSS边框`<border-style>`

>边框各边：`border-top-style`<br>`boder-right/left-style`<br>`border-bottom-style`

`p.dotted{border-style:dotted;}`
`p.mix{border-style:dotted dashed solid double;}`混合边框

1.属性设置
|属性值|效果|
|---|---|
|dotted|点线边框|
|dashed|虚线边框|
|solid|实线边框|
|double|双边边框|
|groove|3d坡口边框|
|ridge|3d脊线边框|
|inset/outset|3dinset/outset边框|
|none|无边框|
|hidden|隐藏边框|

附：
- 如果`border-style`属性设置4个值，则分别对应<i>top，right，bottom，left</i>
- 如果该设置3个值，则分别对应<i>top,right & left,bottom</i>
- 如果2个值，<i>top & bottom,right & left</i>
- 如果1个值，应用于all。

2.边框颜色<br>
`border-color`<br>

也可以使用RGB，HEX，HSL值。

3.边框宽度<br>
`border-width:xxpx;`<br>
`border-width:xxpx yypx;`对应top & bottom，right & left。

### CSS伪类`selector:pseudo-class{property:value;}`

>伪类用于定义元素的特殊状态。
>1.设置鼠标悬停在元素上时的样式<rb>
2.为已访问和未访问链接设置不同的样式<br>
3.设置元素获得焦点时的样式
___
#### 锚伪类(anchor伪类)
以不同方式显示链接`a:pseudo{property:value;}`
>a:link {color:#FF0000;} /* 未访问的链接 */<br>
a:visited {color:#00FF00;} /* 已访问的链接 */<br>
a:hover {color:#FF00FF;} /* 鼠标划过链接 */<br>
a:active {color:#0000FF;} /* 已选中的链接 */<br>

注意：<br> 
1.在CSS定义中，a:hover 必须被置于 a:link 和 a:visited 之后，才是有效的。

2.在 CSS 定义中，a:active 必须被置于 a:hover 之后，才是有效的。

3.伪类的名称不区分大小写。

#### CSS first-child伪类
>使用该伪类来选择父元素的第一个子元素。

- examlpe 1:<br>
>匹配第一个`<p>`元素：
>p:first-child<br>
{<rb>
    color:blue;<br>
}
这里`<p>`作为任何元素的第一个子元素。

- example 2：<br>
>匹配所有` <p> `元素中的第一个 `<i> `元素：
> p i:first-child {<br>
  color: blue;<br>
}
