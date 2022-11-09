# 1.___关联本地repository和github上的repository___

1.__“连接”命令行__
>`$ git remote add origin git@github.com:Anxxx/repository name.git`

（origin是给git远程库指定名字的默认名字，可改,写个add fuck git也行。）
（如果git bush不是在本地repository打开，这场寻亲就会失败。）

2.__push命令行__
>`git push -u origin master`

首次连接SSH会出示警告，yes之后就不会再出现。
之后修改文件后，add+commit再直接只输入`git push`就可以了。

# ___2.删除github上的repository（解绑）___
(就是本地repository和寻亲寻上的那个远程库的解绑)
`git remote rm<name>` name指远程库的名字

附：建议解绑前查看远程库的信息：`git remote -v`

#___3.克隆github repository到本地repository___
命令行：`git clone git@github.com:Anxxx/远程库名.git`

(`ls`可以查看该repository已有文件)
w