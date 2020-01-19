# svn增量文件归档确认

功能：

实现对比excel中的归档登记信息是否与svn归档对齐

做这东西有什么意义？

当然是在自己公司特定场景使用的，不过在家里开发，直接传到git上，去公司再弄下来。

使用方法：

1. 先配置config.py文件，一般来说更改对应版本文件即可
2. 配置定时任务，启动python RefreshConfirm.py



设计框架：

- config.py

  配置文件

  - svnpath

    svn库地址

    - 刷包excel地址
    - upgradetool路径地址
    - javabin地址
    - ILOG地址
    - 可能存在的其他地址

  - localpath

    svn存档地址

    - 'upgradepath':11,
    - 'javabinpath':22,
    - 'Ilogpath':33,
    - 'excelpath':44,
    - 'other':55

  - sshinfo

    linuxssh信息

    - 'hostname'='127.0.0.1',
    - 'port'=22,
    - 'username'='user',
    - 'password'='12345'

  - report

    报告输出

    - 'shellOut':'XX.txt',
    - 'excelOut':'YY.xlsx'

- python主流程：

  - 打印配置文件信息进行确认
  - (TODO)根据config.py生成最新的config.ini
  - 根据**linuxssh**，建立后台连接**trans**
  - 调用shell脚本生成增量更新文件**shellOut**
  - trans下载**shellOut**到本地报告保存地址，关闭**trans**
  - 解析刷包excel，保存到**Data_E**
  - 分析**Data_S**和**Data_E**
  - 保存到**REPORT**

- 建立后台连接**trans**

  - 导入paramiko
  - 读取linuxssh配置，建立后台ssh连接
  - (TODO)确认是否已有shell脚本存在，不存在则上传，并修改权限为755
  - config.py文件上传到后台
  - 调用shell脚本

- shell脚本生成增量更新文件**shellOut**

  - 根据指定目录提取增量更新信息
  - 首次svn checkout(最好人工在归档当晚先行一次)
  - svn update文件，获取增量文件保存到列表
    - 从路径中提取文件名保存到shell更新组
  - 对增量文件列表内地址 svn info
  - (TODO)对增量文件列表内地址 svn log读取最近一行
  - 保存到文件供python解析，格式为**Data_S**
  
- python读取刷包excel 并解析

  - 导入openpyxl
  - 读取修改文件
    - 从路径中提取文件名
    - 筛选分类cpp、jar、war、sh、sql、cfg、其他保存到excel更新组
  - 读取日期
  - 读取开发人员
  - 读取回归情况
  - 保存为**Data_E**类型

- 对比excel更新组和shell更新组

  - 多条记录的，比对最近日期
  - 不存在的，输出到报告
  - 存在的，是否且Last Changed Date和**日期**在一个小时内
    - 在一个小时内，不加入报告
    - 不在一个小时内，输出报告，便于人工核对

- (TODO)将报告发送邮件到个人

- 格式定义

  - Data_S

    - 从svn获取的文件增量更新信息
    - Operation,FilePath,Revision,ChangedAuthor,ChangedDate

  - Data_E

    - 编号，修改文件，文件类型，开发人员，测试人员，转测状态，状态日期，测试状态

  - report

    报告内容涉及

    - Filename,Author,Last Changed Date,Revision,note
    - 需求名称(非必须)
    - 当前状况(非必须)
    - 回归情况(非必须)