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
  >'>>> name=input()
  kim chaewon
  >'>>> name
  'kim chaewon'
  >'>>> print(name)
  kim chaewon

- 在.py文件里输入
  >name=input('don\'t say you are ditto')
   print(name)
---
**输出**

print（）函数

例子：
>`print('100+200')`——100+200
`print(100+200)`——300
`print('ditto','attention')`——ditto attention

---
**换行**
指在交互界面
>'>>>print('''i
...said
...i
...likt it like that''')

<font size='1'>`...`是转行回车之后自动出现的。</font>
---
**列表**

>`>>> name=['minji','haerin']`
`>>> name`
`['minji','haerin']`
`>>>print(name)`
`['minji','haerin']`
`>>> len(name)`
`2`

**列表索引**

>`>>> name[0]`
`'minji'`
`>>> name[-1]`
`'haerin'`

**追加、插入、删除**
