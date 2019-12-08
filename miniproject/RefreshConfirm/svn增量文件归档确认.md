# svn增量文件归档确认

功能：

实现对比excel中的归档登记信息是否与svn归档对齐



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
    - 'username'='billing',
    - 'password'='12345'

  - report

    报告输出

    - 'shellOut':'updatelist_time.txt',
    - 'pythonOut':'updatelist_time.xlsx'

- python主流程：

  - 打印配置文件信息进行确认
  - 根据config.py生成最新的config.ini
  - 根据**linuxssh**，建立后台连接**trans**
  - 调用shell脚本生成增量更新文件**shellOut**
  - trans下载**shellOut**到本地报告保存地址，关闭**trans**
  - 解析刷包excel，保存到**pyparse对象**
  - 分析**shellOut**和**pyparse**
  - 保存到**pythonOut**

- 建立后台连接**trans**

  - 导入paramiko
  - 读取linuxssh配置，建立后台ssh连接
  - 确认是否已有shell脚本存在，不存在则上传，并修改权限为755
  - config.py文件上传到后台
  - 调用shell脚本

- shell脚本生成增量更新文件**shellOut**

  - 首次svn checkout(最好人工在归档当晚先行一次)
  - svn update文件，获取增量文件保存到列表
    - 从路径中提取文件名保存到shell更新组
  - 对增量文件列表内地址 svn info
    - Revision
    - Author
    - Last Changed Date
  - 对增量文件列表内地址 svn log读取最近一行
  - 保存到文件供python解析

- python读取刷包excel 并解析

  - 导入xlrd，xlsxwriter
  - 读取修改文件
    - 从路径中提取文件名
    - 筛选分类cpp、jar、war、sh、sql、cfg、其他保存到excel更新组
  - 读取日期
  - 读取开发人员
  - 读取回归情况

- 对比excel更新组和shell更新组

  - 多条记录的，比对最近日期
  - 不存在的，输出到报告
  - 存在的，是否且Last Changed Date和**日期**在一个小时内
    - 在一个小时内，不加入报告
    - 不在一个小时内，输出报告，便于人工核对

- 格式定义

  - shellOut

    - Filename,Author,Last Changed Date,Revision
    - 开关控制，追加第六列URL

  - pyparse

    - 修改文件，开发人员，日期，回归情况

  - pythonOut

    报告内容涉及

    - Filename,Author,Last Changed Date,Revision,note
    - 需求名称(非必须)
    - 当前状况(非必须)
    - 回归情况(非必须)