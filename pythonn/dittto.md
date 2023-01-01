# python学习
## 基础
---
### 基础1

>文件格式——**.pv**

>python字符串类型为str，在网络上传输或者保存到磁盘使用str变为以字节为单位的bytes。使用.encode('ascii')

>**数据类型**
<font size='1'>python可以直接处理的数据类型：</font>
  <font size='2'>（1）整数
（2）浮点数
（3）字符串
（4）布尔值——True False，and 与运算，or或运算，not非运算
（5）空值
（6）变量
（7）常量：大写变量名表示常量</font>



#### 输入与输出
---
**输入**
- 在交互终端输入：`input()函数`
  >'>>> name=input() <br>
  kim chaewon <br>
  >'>>> name <br>
  'kim chaewon' <br>
  >'>>> print(name) <br>
  kim chaewon

- 在.py文件里输入
  >name=input('don\'t say you are ditto')<br>
   print(name)
   s=int(input('example:'))
---
**输出**

print（）函数

例子：
>`print('100+200')`——100+200 <br>
`print(100+200)`——300 <br>
`print('ditto','attention')`——ditto attention

---
**换行**
指在交互界面
>'>>>print('''i<br>
...said<br>
...i<br>
...likt it like that''')

><font size='1'>`...`是转行回车之后自动出现的。</font>
---
**列表**

>`>>> name=['minji','haerin']` <br>
`>>> name` <br>
`['minji','haerin']` <br>
`>>>print(name)` <br>
`['minji','haerin']` <br>
`>>> len(name)` <br>
`2`

**列表索引**

>`>>> name[0]` <br>
`'minji'` <br>
`>>> name[-1]` <br>
`'haerin'`

**追加、删除，插入**
|追加|删除|插入|替换|
|---|---|---|---|
|.append()|.pop()|.insert()|xxx|
|`>>> name.append('hyein')`<br>默认追加到最后一个<br>`>>> name`<br>`['minji','haerin','hyein']`|`>>> name.pop()`<br>括号内空默认删除末尾元素<br>`>>>> name.pop(0)`<br>`'minji'`<br>`>>>> name`<br>`['haerin']`|`>>> name.insert(1,'hyein')`<br>`>>> name`<br>`['minji','hyein','haerin']`|`>>> name[1]='hyein'`<br>`>>> name`<br>`['minji','hyein','haerin']`|


#### 函数的参数

---
**位置参数**

example:
>def test(x,n)

`x` 和`n`就是位置参数，调用函数时，传入的两个值按照位置顺序依次赋值给参数`x`和`n`。

---
**默认参数**

example:
>def test(x,n=3)

调用test函数只需输入`x`的值，即`test(5)`，相当于调用`test(5,3)`

注意：
- （1）必选参数在前，默认参数在后。否则会报错。
- （2）多个参数时将变化大的参数放在前面，变化小的参数放后面。变化小的参数作为默认参数。
- （3）默认参数必须指向不变对象。
- （4）`def test(name,gender='f'):`<br>
    `print('name:',name)`<br>
    `print('gender:',gender)`<br>
`test('yujin','m')`<br>
`name: yujin`<br>
`gender: m`

---
**可变参数**<br>
<font size=2>可变指传入的参数个数是可变的，0到任意个。</font>

> `def test(*numbers):`<br>
    `sum=0`<br>
    `for n in numbers:`<br>
        `sum=sum+n*n`<br>
    `return sum`<br>
`print(test(1,2,3))`

参数`n`内部接收到的是一个tuple。

ps:
如果已经有了一个list或tuple，调用一个可变参数的两种方法：
>`n=[1,2,3]`<br>
`test(n[0],n[1],n[2])`

>`n=[1,2,3]`<br>
`test(*n)`——*n表示把该list所有元素作为可变参数传进去。

---

**关键字参数**
该参数允许传入任意个含参数名的参数，这些关键字参数在函数内部自动组成一个dict。
关键字参数可以拓展函数功能。

>`def ra(name,age,**more):`
  `print('name:',name,'age:',age,'other:',more)`

>`extra={'food':'melo','music':'deja vu'}`<br>
`ra('minji',19,**extra)`

>name:minji age:19 other:{'food':'melon','musci':'deja vu'}

`**extra`表示把`extra`这个dict所有key-value用关键字参数传入函数的`**more`参数，`more`将获得一个dict——`extra`的拷贝，修改`more`不会影响`extra`。

---

**命名关键字参数**
如果要限制关键字参数的名字，就可以用命名关键字参数。

>`def people(name,age,*,city,job):`<br>
  `print(name,age,city,job)`<br>
`*`后面的参数被视为命名关键字参数。

调用方式：
>`people('yujin',19,city='seoul',job='dancer')`

- 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`。
- 命名关键字参数必须传入参数名。否则将报错。
- 命名关键字参数可以设置默认值。传入时可以不传入已设置默认值的参数。
  
---

**参数组合**

>- 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。

>- 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


定义一个函数：
>`def test1(a,b,c=0,*x1,**x2):`<br>
`print('a=',a,'b=',b,'c=',c,'x1=',x1,'x2=',x2)`


测试一：
>`test1(1,2,c=3,'a','b',ditto=oh)`<br>

结果：
>a=1 b=2 c=3 x1=('a','b') x2={'ditto':oh}

测试二：
>`x1=(1,2,3,4)`<br>
`x2={'priority':good,'s':'&'}`<br>
`test1(*x1,**x2)`

结果：
>`a=1 b=2 c=3 x1=(4,) x2={'priority':good,'s':'&'}`


- 虽然可以组合多达5种参数，但不要同时使用太多组合，否则函数接口的可理解性很差。