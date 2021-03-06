# Python感应篇

作为一个为时不过2小时的教程，我们对python能做到的也仅此感应而已。

## 【**总纲**】

[TOC]

> 不是重点的部分，都不会细说，重点部分用【】标记
>
> 比如，我们不纠结，python是脚本语言还是编程语言，它显然是脚本语言，也属于编程语言，此题终结。	
>
> 不是所有写下来的部分都需要一一说明，很多东西只是指引，作为你的课后参考
>
> 教学主要以所学即作的形式进行。
>
> 

## 【预研心要】

1. 你所需要了解的知识
3. python的方向

大概会耗费你十分钟，了解这些我们进入正式课程，正式课程会通过**jupyter notebook**开始演示。



有人问过，为什么现在搞人工智能都用python，这个是**伪命题**，不是都用python，各种语言都有的。很多强大的人工智能算法库都依赖于C/C++编译的dll。这里就要谈谈 python的优势。



Python语言写的程序不需要编译成二进制代码。可以直接从源代码运行程序。

在计算机内部，Python解释器把源代码转换成称为字节码的中间形式，然后再把它翻译成计算机使用的机器语言并运行。

### python优势

1. 几乎所有的linux机器上都有预装。
2. 容易学习，阅读，编写和调试，开发效率高。
4. 广泛的工具库
4. 自动内存管理

### 工具使用

python: https://www.python.org/downloads/



1. [pycharm]: https://www.jetbrains.com/pycharm/

   

2. [Visual Code]: https://code.visualstudio.com/

   

3. [anaconda]: https://www.anaconda.com

   自带**jupyter notebook**的发行版



python版本多？

遇事不决，下最新版

### **python的劣势**

1. 运行效率低于c和java，在批量处理和大规模运算中尤其明显。（不过可以用一些c编译的库提升效率）
2. GIL全局锁，任何时候，一个进程内的多线程都是无法利用到多核CPU的效率

### 【理念确定】

非专业开发人员学习编程工具应该给自己设定的**学习方向**。

1. 编程语言是为了**达成目的**的**工具**。
2. **分配**合理的**时间**在对应的**方向**。

基于以上两点。首先确定。

我们学习编程语言**能干什么**。

对于测试来说，实现**测试自动化**，同样，对于其他业务来说，处理大量数据，节省人力。

我们能将**主要精力**放在这上面吗？

不推荐，python可以做很多工具，但是有更多的是现成的工具使用，对于现在的节奏来说，python能当做一种潮流行技能，他们学了，我也不能落后。但我同样可以学习更多他们所未学到的技能。

python的库那么多，该怎么学？

什么常用或者需要什么，那么这就是你首要学习的目标，其次，可以将热门的方向作为你学习的方向。

- 数据科学

- 机器学习
- 网站开发
- 自动化工程
- 网络爬虫

### 在项目组中我们能用py做什么

以测试组为例，目前有不少python小工程已经在运作了，比如 知识库爬取，获取我们的发帖情况，或者测试报告生成到excel展示，监测问题进行邮件群发，测试用户数据生成，dcc消息转发，归档脚本检测，挑单流程自动化工具。

### 脚本演示

- 从我的仓库中扣各种库的东西下来看看就行

1. DccRouter
2. UserDataGenerator
3. FileChecker

> 接下来的部分，就是要为我们打下python这块领域的地基了，代码由jupyter notebook



# 【Python上篇】

> 上篇概述：输出交互与简单规范及字符串处理

1. 与界面的交互

2. 使用注释内容或# TODO辅助思路

3. 代码编写规范tab或者4blank

4. 字符串与数字

5. 对象属性查看

   

   


# 【Python中篇】

> 中篇概述：数据类型与函数

1. 列表list
2. 元组tuple
3. 集合set
4. 字典dict
5. 数据类型特性
6. 函数与参数
7. if表达式

   

## 【Python中篇】

> 中二概述：逻辑加深与异常处理

1. while循环
2. for循环
3. try/except/finally异常处理


# 【Python下篇】

> 下篇概述：读写文件与模块导入与类的继承

1. 文件读写
2. 模块安装
3. 类(class)
4. Functions
5. Classes & Objects
6. Object Functions
7. Inheritance

# 【Python X篇】

> 所未提及，亦需自习

1. python代码规范

2. os处理

3. sys读取参数

4. csv处理

5. sort 排序

6. schedule 定时任务

7. re 正则表达式

8. time/datetime 时间模块

9. random 随机

10. pycharm deploy 远端部署

11. pycharm debug   调试

12. pickle 对python对象存储与读取

13. functools 

14. itertools  迭代器

15. collections 

16. operator 运算符 

17. Unittest 单元测试

18. globals,locals

19. 垃圾回收

    




# 课后

## **总结**

我们这堂课的效果是要做到连你的女朋友都能学会的python，好的，问题来了，你女朋友都会了，而你却还不会，多丢面子，回去赶紧偷偷练习。你学会了，又可以来教你女朋友了。



课后记得复习，学过的东西，不是马上就能掌握的，没有实践过的代码，都是纸上谈兵。复习一遍，巩固知识，再看一遍，深入理解，要是再来一遍，浪费时间，还不如敲代码。


## 书籍推荐

入门加进阶

1. 廖雪峰python3教程

2. 笨办法学 Python(第四版）

3. Python+Cookbook

4. [python官方]: https://docs.python.org/zh-cn/3/library/index.html

   

进阶书籍很多，现在无需推荐，因为都有各自的侧重点。我建议你们通过入门书籍掌握python的基础能力，在之后学习的过程中，根据自己应用的方向，可以去查找，而收藏不是为了打入冷宫

【**初学者练习不要复制粘贴**】