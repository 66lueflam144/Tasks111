*`cascading style sheets`*

# __CSS__ 
>*__释义一__*：一种用来为结构化文档（HTML文档或XML应用）添加样式的计算机语言，其文件扩展名为`.css`。<br>
>*__释义二__*：将样式信息与网页内容分离的一种语言，为每个元素定义样式，主要用于美化HTML页面。

ps:HTML标签构成了网页的基本结构，只是一个框架，CSS就是来装修的。
## &Delta;__CSS作用__
>通过设置对应的css样式属性可以修改HTML文档内各元素的显示，位置等样式。

## &Delta;__CSS语法__

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

## &Delta;CSS伪类`selector:pseudo-class{property:value;}`

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

- example 3.<br>
>选择器匹配作为另一个元素的第一个子元素的 <p> 元素中的所有 <i> 元素：
p:first-child i {<be>
  color: blue;<br>
}


#### CSS :lang伪类

>允许您为不同的语言定义特殊的规则

#### other CSS伪类
<b></b><a href=https://www.w3school.com.cn/css/css_pseudo_classes.asp>CSS伪类whole</a></b>


## &Delta;CSS盒模型（box model）

&euro;`控制元素和元素之间，或者元素和内容之间的位置关系；`
- <a href=https://www.runoob.com/css/css-boxmodel.html>runoob CSS box model参考</a>
- <a href=https://zhuanlan.zhihu.com/p/264250523>知乎CSS box model参考</a>
- <a href=https://www.php.cn/css-tutorial-409334.html>CDSN CSS box model参考</a>
- <a href=https://www.cnblogs.com/qianguyihao/p/7256371.html>cnblogs CSS box model参考</a>
___
box model<br>
<img src=https://www.runoob.com/images/box-model.gif />


>&hearts;Margin(外边距) - 清除边框外的区域，外边距是透明的。<br>
&hearts;Border(边框) - 围绕在内边距和内容外的边框。<br>
&hearts;Padding(内边距) - 清除内容周围的区域，内边距是透明的。<br>
&hearts;Content(内容) - 盒子的内容，显示文本和图像。


<img src=http://img.smyhvae.com/2015-10-03-css-27.jpg /><br><br>

<img src=http://img.smyhvae.com/2015-10-03-css-30.jpg />

>&clubs;最终元素的总宽度计算公式是这样的：<br>
总元素的宽度=宽度+左填充+右填充+左边框+右边框+左边距+右边距<br>

>&clubs;元素的总高度最终计算公式是这样的：<br>
总元素的高度=高度+顶部填充+底部填充+上边框+下边框+上边距+下边距<br>

如果元素的宽度（width）一定的情况下，W3C盒模型的宽度（width）不包括内边距和边框，IE盒模包括。&diams;
CSS盒模型和IE盒模型的区别：

>*在 标准盒子模型中，width 和 height 指的是内容区域的宽度和高度。增加内边距、边框和外边距不会影响内容区域的尺寸，但是会增加元素框的总尺寸。*<br>
*IE盒子模型中，width 和 height 指的是内容区域+border+padding的宽度和高度。*
    
  附：一些用法<br>
<img src=https://github.com/66lueflam144/Tasks111/blob/main/web.ufo/%E7%9B%92%E6%A8%A1%E5%9E%8B1.png />    
  <br>
  <img src=https://github.com/66lueflam144/Tasks111/blob/main/web.ufo/%E7%9B%92%E6%A8%A1%E5%9E%8B2.png />  


___
## CSS position定位（5 kinds）
`CSS 中的 position 属性用来设置元素在页面中的位置，通过该属性您可以把任何属性放置在任何您认为合适的位置。position 属性有 5 个可选值`


<a href=http://c.biancheng.net/css3/position.html>CSS position参考1</a><br>
<a href=https://blog.csdn.net/qq_35508835/article/details/115573672>CSS position参考2</a>
___
- <b>static(正常定位)：</b>position属性默认值。且当为该属性值时，top，right。bottom,left,z-index均不生效。
- <b>relative（相对定位）</b>：通过 top、right、bottom、left 这 4 个属性来设置元素相对于正常位置的偏移量，在此过程中不会对其它元素造成影响。
- <b>absolute（绝对定位）</b>：相对于第一个非 static 定位的父级元素进行定位，可以通过 top、right、bottom、left 这 4 个属性来设置元素相对于父级元素位置的偏移量。如果没有满足条件的父级元素，则会相对于浏览器窗口来进行定位。使用绝对定位的元素不会对其它元素造成影响。
- <b>fixed(固定定位)</b>:相对于浏览器的创建进行定位，可以使用 top、right、bottom、left 这 4 个属性来定义元素相对于浏览器窗口的位置。使用固定定位的元素无论如何滚动浏览器窗口元素的位置都是固定不变的。
- <b>sticky(粘性定位):</b>它是 relative 和 fixed 的结合体，能够实线类似吸附的效果，当滚动页面时它的效果与 relative 相同，当要滚动到屏幕之外时则会自动变成 fixed 的效果。

___
## CSS布局



### <i>版本一</i>
|布局|描述|
|---|---|
|传统盒模型布局|xxx|
|文档流布局|按照文档的顺序一个一个显示出来，块元素独占一行，行内元素共享一行|
|浮动布局|浮动方式布局就是使用 float 属性，使元素脱离文档流，浮动起来|
|定位布局|可以通过 position 属性来进行定位|
|flex布局|为盒状模型提供最大的灵活性，使用该布局方式可以实现几乎所有你想要的效果|

### <i>版本二</i>

<img src=https://ask.qcloudimg.com/http-save/yehe-6353923/8r1gyeun0r.jpeg?imageView2/2/w/1620 />

<a href=https://cloud.tencent.com/developer/article/1515810>原文参考</a>
