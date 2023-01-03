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
##### **输入**
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
##### **输出**

print（）函数

例子：
>`print('100+200')`——100+200 <br>
`print(100+200)`——300 <br>
`print('ditto','attention')`——ditto attention

---
##### **换行**
指在交互界面
>'>>>print('''i<br>
...said<br>
...i<br>
...likt it like that''')

><font size='1'>`...`是转行回车之后自动出现的。</font>
---
##### **列表**

>`>>> name=['minji','haerin']` <br>
`>>> name` <br>
`['minji','haerin']` <br>
`>>>print(name)` <br>
`['minji','haerin']` <br>
`>>> len(name)` <br>
`2`

##### **列表索引**

>`>>> name[0]` <br>
`'minji'` <br>
`>>> name[-1]` <br>
`'haerin'`

##### **追加、删除，插入**
|追加|删除|插入|替换|
|---|---|---|---|
|.append()|.pop()|.insert()|xxx|
|`>>> name.append('hyein')`<br>默认追加到最后一个<br>`>>> name`<br>`['minji','haerin','hyein']`|`>>> name.pop()`<br>括号内空默认删除末尾元素<br>`>>>> name.pop(0)`<br>`'minji'`<br>`>>>> name`<br>`['haerin']`|`>>> name.insert(1,'hyein')`<br>`>>> name`<br>`['minji','hyein','haerin']`|`>>> name[1]='hyein'`<br>`>>> name`<br>`['minji','hyein','haerin']`|


#### 函数的参数

---
##### **位置参数**

example:
>def test(x,n)

`x` 和`n`就是位置参数，调用函数时，传入的两个值按照位置顺序依次赋值给参数`x`和`n`。

---
##### **默认参数**

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
##### **可变参数**<br>
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

##### **关键字参数**
<br>
该参数允许传入任意个含参数名的参数，这些关键字参数在函数内部自动组成一个dict。
关键字参数可以拓展函数功能。

>`def ra(name,age,**more):`
  `print('name:',name,'age:',age,'other:',more)`

>`extra={'food':'melo','music':'deja vu'}`<br>
`ra('minji',19,**extra)`

>name:minji age:19 other:{'food':'melon','musci':'deja vu'}

`**extra`表示把`extra`这个dict所有key-value用关键字参数传入函数的`**more`参数，`more`将获得一个dict——`extra`的拷贝，修改`more`不会影响`extra`。

---

##### **命名关键字参数**
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

##### **参数组合**

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

---

#### **递归函数**

例子：
>`def fun(n):`<br>
`if n==1:`<br>
`return 1`<br>
`return n*fun(n-1)`

- 使用递归函数需要注意防止栈溢出。
- 解决递归调用栈溢出的方法是尾递归优化——事实上尾递归和循环的效果一样——尾递归是指，在函数返回的时候，调用自己本身，并且，return语句不能包含表达式。这使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
  

尾递归形式：  
>`def fun(n):`<br>
`return ction(n,1）`

>`def ction(m,p):`<br>
`if m==1:`<br>
`return p`<br>
`return ction(m-1,m*p)`

- python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

---
#### **高级特性**

---

##### **切片**
<br>

----

**LIST**：
>`L=['a','b','c','d','e']`<br>
`s=L[0:3]`<br>
`print(s)`

结果为：
>`['a','b','c']`

即从索引0开始到索引2，不包括索引3。

- 索引0可以省略——`L[:3]`
- `L[1:4]`即从索引1开始到索引3结束。
- `L[-1:]`即倒数第一个数
- `L[::5]`每5个取一个，从索引0开始。
- `L[:3:2]`前3个数，每2个取一个。
- `L[:]`原样复制。

---

- tuple或者字符串也可以使用切片。

----

##### **迭代**

>如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代。

| `list`or `tuple`or 字符串| **`dict`**|
|---|---|
|`for value in values`|`for value in d.values`<br>`for k(,v)in d.items`|
|例子：<br>`for x in s`|例子：<br>`d={'x':'money','y':'why','z':'hey'}`<br>`for k,v in d.items():`<br>`print(k,'=',v)`|

- 打印索引-元素对(enumerate函数)：<br>`for i,value in enumerate(['a','b'])`<br>`0 a`<br>`1 b`
- 同时引用多个变量：`for x,y in [(1,2),(2,3)]`
  
----

##### **列表生成式**

>生成list使用`list(range(1,11))`——1到10.

>`[x*x for x in range(1,11)]`<br>即`L=[]`<br>`for x in range(1,11):`<br>`L.append(x*x)`

- for循环后面还可以加上if判断。
- 还可以使用两层循环，生成全排列。
- `if...else`使用例子：`[x if x%2==0 else -x for x in range(1,11)]`——**在一个列表生成式中，`for`前的`if...else`是表达式，而`for`后面的`if`是过滤条件，不能带`else`。**

<br>

|if判断|两层循环|两个变量|
|---|---|---|
|`[x*x for x in range(1,11) if x%2==0]`|`[m+n for m in 'money' for n in 'lisa']`|`d={'x':'a','y':'b','z':'c'}`<br>`[k + '=' + v for k,v in d.items()]`|

---

##### **生成器**

>一边循环一边计算的机制

`g=(x*x for x in range(10))`<br>
- list和generator区别在于`[]`和`()`
- 使用for循环打印（generator也是可迭代对象）：<br>`for n in g:`<br>`print(n)`
- 用`for`循环调用generator时拿不到`return`语句的返回值，如果想拿到返回值，必须捕获`StopIteration`错误，返回值包含在`StopIteration`的`value`中。
- generator函数在执行过程中，遇到`yield`就中断，下次又继续执行。

<a href=https://www.liaoxuefeng.com/wiki/1016959663602400/1017318207388128>生成器应用的具体例子</a>

---


##### **迭代器**


>可以被`next()`函数调用并不断返回下一个值的对象被称为迭代器：`Iterator`。

- 生成器都是`Iterator`对象，但`list`,`dict`,`str`是`Iterable`不是`Iterator`。使用`iter()`函数可以将其变成`Iterator`。

---

#### **函数式编程**

----

##### **高阶函数**
>一个函数接收另一个函数作为参数，该函数称为高阶函数。

example：`def add(x,y,f):`<br>$~~~~~~~~~~~~~~~~~~~~$`return f(x)+f(y)`<br>其中f传入一个函数如`abs`。

---

**map/reduce**

>`map()`函数接收两个参数，一个是函数，一个是`Iterable`。`map()`将传入的函数依次作用到序列的每个元素，并把结果作为新的`Iterator`返回。


例子：<br>
`def f(x):`<br>
$~~~~~~$`return x*x`<br>
`r=map(f,[1,2,3])`<br>
$~~~~~~$`print(list(r))`<br>
得到结果：`[1,4,9]`
- 结果r是一个`Iterator`——惰性序列——因此通过`list()`函数让它把整个序列都计算出来并返回一个list。
  
>`reduce()`把一个函数作用在一个序列[x1,x2,x3,x3...]上，该函数必须接收两个参数。

例子：<br>
`from functools impot reduce`<br>
`def add(x,y):`<br>
$~~~~~~~~$`return x+y`<br>
`print(reduce(add,[1,2,3]))`<br>

结果是6

<br>感觉常用于转换数据类型。


ps：
>函数本身可以赋值给变量，即变量可以指向函数。
example:`f=abs`<br>`f(-10)`

>函数名是指向函数的变量。

---

### **面向对象编程**

>Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

>在python中，所有数据类型都可以视为对象，也可以自定义对象（自定义的对象数据类型就是面向对象中的类class的概念）。

>面向对象的设计思想是抽象出class，根据class创建实例（instance）。

----

#### **类和实例**

|类 |实例 |
|---|---|
|类是创建实例的模板 |实例是一个一个具体的对象，各个实例拥有的数据互相独立，互不影响 |
|定义类通过`class`关键字|根据类名+（）创建实例 |
| `class dally(object)`|`test=dally()`|
|`class`是关键字，`dally`是类名。`(object)`表示该类是从哪个类继承下来的，通常无合适继承类就使用`object`。 |变量`test`指向一个`dally`的实例。 |

>在类中定义的函数第一个参数永远是实例变量`self`，并且调用时不用传递该参数。

---

#### **数据封装**

>类本身拥有一些数据，直接在类的内部定义访问数据的函数，这样就将数据封装起来了。
ps：
- 这些封装数据的函数时和类本身关联的，称为**类的方法**
- 好处是可以给类增加新的方法以及隐藏内部实现细节。

>定义一个方法，除了第一个参数是`self`外，其他和普通函数一样。调用一个方法只需在实例变量上直接调用，除了`self`不用传递，其他参数正常传入。

---

#### **访问限制**

>如果让内部属性不被外部访问，可以把属性的名称前加上两个下划线`_`。<br>实例的变量名以`_`开头，就变成一个私有变量——只有内部可以访问，外部不可以访问。

>`_xxx_`是特殊变量名，可以直接访问。

- 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
- 可以通过`_class_变量名`的方式来访问`_变量名`这个私有变量。
  
---

#### **继承和多态**



>在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类，而被继承的class称为基类、父类或超类。

>继承的最大好处是子类获得了父类的全部功能。


例子：
`class animal(object):`<br>
$~~~~~$`def run(self):`<br>
$~~~~~$`print('animal is running...')`<br>
$~~~~~~~~~~~~~~$
`class dog(animal):`<br>
 $~~~~~$`pass`

`dog=dog()`<br>
`dog.run()`

结果为：animal is running...

---


>当子类和父类存在相同的方法时，子类的方法可以覆盖父类的same方法，，代码运行时总是调用子类的方法，这样，获得了继承另一个好处——多态。

ps：
- 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行。
- 开闭原则：
  - 对扩展开放：允许新增子类
  - 对修改封闭：不需要修改依赖父类的各种函数。

---

#### **获取对象信息**

|`type()` |`isinstance()` |`dir()`|
|---|---|---|
|（1）判断对象类型<br>（2）判断指向函数或类的变量|判断class的类型。|获得一个对象的所有属性和方法|
|`type(123)` |`isinstance(变量,class) `|`dir()`|
<br>
ps：

- `type()`判断的基本类型也可以用`isinstance()`判断。（`isinstance(123,int)`）

---

#### **实例属性&类属性**

- 实例属性——通过实例变量或者`self`变量给实例绑定属性
- 类属性——直接在class定义中定义的属性



----

### **关于文件的操作**

#### **文件操作**

##### **文件打开与关闭**

|打开&emsp;open()|关闭&emsp;close()|
|---|---|
|`f=open('/path/to/file','r')`|`f.close()`|
|如果文件打开成功，调用`read()`方法一次性读取全部内容。|文件使用完毕后必须关闭|


不过常用版本是：
>`with open('/path/to/file',r') as f:`<br>$~~~~$`print(f.read())`

(作为`try:`<br>$~~~~~$`f=open('path/to/file','r')`<br>$~~~~~$`print(f.read())`<br>`finally:`<br>$~~~~~$`if f:`<br>$~~~~~~~~~~$`f.close()`<br>的简化版)

- 调用不确定大小的文件，为了保险起见，需要反复调用`read(size)`方法。
- 配置文件，调用`readlines()`发发最方便。

----
##### **写文件**

基本与读取文件一致，区别在于调用`open()`函数，传入标识符为`w`或`wb`。

例子：<br>
`f=open('/path/to/file','w')`<br>$~~~~~~~$`f.write('i dot to ride til i die die')`<br>$~~~~~~~$`f.close()`

或者(常用)<br>
`with open('/path/to/file','w') as f:`<br>$~~~~~~~$`f.write('antitifragile')`

- 如果以`w`模式写入文件时，文件已经存在，会直接覆盖——相当于删除后重新写入一个文件。
- 如果希望追加内容到文件末尾，传入`a`以`append`模式写入。

----

##### **StriIO和BytesIO**

|StringIO|BytesIO|
|---|---|
|在内存中读写str|在内存中读写bytes|
|`from io import StringIO`|`from io import BytesIO`|

---

##### **操作文件和目录**

python交互式命令行中使用`os`模块。

- *查看当前目录的绝对路径*：<br>`os.path.abspath('.')`
- *在某个目录下创建一个新目录*：
  - *首先把新目录的完整路径表示出来*：<br>`os.path.join('/path/to','testdir')`
  - *然后创建一个目录*：<br>`os.mkdir('/path/to/testdir')`
  - *ps:删掉一个目录*：`os.rmdir('path/to/testdir)`
  

<a href=https://www.liaoxuefeng.com/wiki/1016959663602400/1017623135437088>more & more</a>

---

##### **序列化**

>把变量从内存中变成可存储或传输的过程称之为序列化.<br><br>序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。<br><br>反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化.


- `pickle.dumps()`直接将对象序列化后写入一个`file-like Object`:<br>`f=open('dump.txt','wb')`<br>`ppickle.dump(d,f)`<br>`f.close()`
- 当我们把对象从磁盘读到内存时，可以先把内容读到一个`bytes`然后用`pickle.loads()`方法反序列化出对象，也可以直接用`pickle.load()`方法从一个`file-like Object`中直接反序列化出对象。


----
（面向对象&emsp;程序设计，创建对&nbsp;象，方法&ensp;定义，调用，掌握面向对象的特性，文件操作，爬取网站资源，如何爬取）