before this starts,<br>`git config user.name`<br>`git config user.email`用于查询<br>
`git config --global user.name 想改的用户名称`
`git config --global user.email 邮箱`用于修改git的全局用户及其email。

`git config user.name想改的名字`
`git config user.email 邮箱`用于修改当前project的用户及其email。

>重新提交就是删除本地repository里的文件，提交删除后，把复制好的文件重新上传is ok。



# ==1.git bush 和 git GUI 的区别：==

*git bush是命令行形式操作入口<br>git GUI是图形化操作入口。<br>执行效果一样，git GUI更方便看。*
***
（所以后续就和git bush命令行学习有关）
***
# 2.创建repository
*first*
打开需要创建repository的地方，打开git bush
>` $ mkdir 文件名`
> `$ cd 文件名`
> `$ pwd`

此时创建了一个目录


*second*
使用`git init`将目录变成git repository
>`$ git init`

使用`ls -ah`可以看到隐藏的`.git`目录，该目录用于git跟踪管理repository，一般不要去搞它，乱搞会导致repository狗带。
***
# 3.添加文件到repository
命令行：
>`$ git add 文件`
>`$ git commit -m<message>`

附：
`文件` 可以一次多个，文件名之间空格即可，git commit的message就要注明“add n files”(后知后觉这里就是打tag方便辨认文件版本![16496AEA](https://user-images.githubusercontent.com/116988892/199697298-c7260efc-7325-4dc0-930f-0a601ec0425d.png)
）

# 4.查看文件的修改
使用`git status`查看文件是否更改以及是否提交更改。
使用`git diff`查看更改记录

附：提交更改后的文件步骤：
>`git add`<br>
>`git status` 这里会提示即将提交更改后文件<br>
>`git commit -m "add distributed"`<br>
>使用`git status`查看状态，显示`working tree clean`就行了。

# 5.reset and log and reflog
首先需要知道，在git中，`HEAD`表示当前版本，上一个就是`HEAD^`（也可以写成`HEAD~1`

想看见`HEAD`，使用`git log`命令，或者打开git GUI查看。

回退版本命令 `git reset --hard 版本or commit id`

附：回退操作的回退：
1.没有关闭命令行窗口且执行过`git log`时，找到所需版本的commit id，使用`git reset --hard`输入前几个commiti id就可以回去了。

2.上述else：使用`git reflog`后可以查看版本记录，之后重复上述操作即可。

（reset不仅回退还可以跳跃）

# 6.撤销checkout
需要了解一下工作区和暂存区相关：<https://www.liaoxuefeng.com/wiki/896043488029600/897271968352576> <br>
撤销命令行`git checkout -- 文件名`
1.丢弃工作区修改，使用撤销命令行<br>
2.丢弃暂存区修改，使用回退版本命令行`git reset HEAD<>`，然后再次使用1.所示方法。

# 7.删除文件
1.删除本地文件（就是repository还查得到前提是你提交了）：<br>`rm 文件名` <br>撤回使用`git checkout --文件名` <br>
2.删除repository里的：`git rm 文件名`+`git commit -m` <br>

# 8.SSH KEYS
本地git repository和github repository是靠SSH加密的。<br>
* 1.打开git bash，输入`ssh-keygen -t rsa -C "email"`，之后一路回车（需要设置密码另说）
* 2.打开github，把`id_rsa.pub`内容cv到add SSH key的key文本框里，add key
* 完结撒花。

附：**SSH的意义**<br>
因为GitHub需要识别出你推送的提交确实是你推送的，而不是别人冒充的，而Git支持SSH协议，所以，GitHub只要知道了你的公钥，就可以确认只有你自己才能推送。<br>

**.shh在用户主目录下，for me it is hxxx**



# 9.创建与合并分支（branch）

1.创建并切换到新分支的命令行：
`git switch -c 新分支名字`（建议常用这个）<br>
`git checkout -b 新分支名字`

(此时提交文件就是提交到新分支上了。)
（查看分支`git branch`)

2.切换分支`git switch/checkout 分支名字`)

3.删除分支`git branch -d 分支名字`

4.合并某分支与当前分支`git merge 某分支名字`<br>合并分支后再删除分支=直接在某分支上工作效果（合并删除重复部分。。可以这样理解吧）

附：
一、分支之间的跳转，需要保证该分支下工作区、暂存区与分支提交相同，无修改：即git diff HEAD 无差异；否则在分支跳转时会出现报错情况，无法跳转

二、分支跳转完成后后，工作区目录会恢复到当前分支最近一次提交下的目录情况，即不同分支底下的目录内容即便存在差异，也不会互相干扰泾渭分明。

例：dev下修改了test.txt文件提交到dev分支（不提交会出现修改差异无法跳转），dev跳转到master之后，工作区目录会恢复到master最近一次提交下的情况，此时查阅test,txt文件并不会看到在dev分支下的修改。

## 9.2 多分支冲突
