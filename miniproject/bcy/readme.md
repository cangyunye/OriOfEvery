# 半次元下载器

## 背景

个人也是二次元爱好者，比较喜欢看看半次元各种cos照，所以简单的下载器

功能：

1. 支持下载无水印原图
2. 支持按用户`uuid`下载所有点赞的文章图片

## 设计方案

参考 
<https://blog.biezhi.me/2018/01/design-and-implement-a-crawler-framework.html>

### 目录结构

bcy/
├── __init__.py
├── log/
├── database/
│   └── __init__.py
├── pics/
│   └── __init__.py
├── downloaders/
│   └── __init__.py
├── html/
├── parsers/
  └── __init__.py
└── bcy_downloader.py

- log目录，保存执行日志

- database目录，将已处理信息记录到数据库

- store，用于分类保存下载的图片，文章，视频

- downloaders，下载器，用于下载文章，视频，图片，音乐

- html，用于保存当前下载的网页

- parsers，用于解析网页

  


### 选择器

1. 选择从“喜欢”页中的文章获取图片
2. 选择从"原作/标签"中获取图片
3. 从热门列表获取图片
4. 获取视频
5. 获取小说
6. 获取文章中评论

INPUT:输入选择方式

OUTPUT:根据选择器的类型输出的url

### URL管理器

队列存储

### 网页下载器

下载网页内容，即保存到content，或者将HTML保存到本地

### 爬虫调度器

获取下载的HTML，传递给解析器

### 网页解析器

提取所需要的数据，如图片地址，视频地址，音乐地址

### 数据处理器

将解析的数据入库或者保存到本地

#### 保存到本地

根据作者分组保存

#### 保存到数据库

用于识别是否已重复下载

### 日志记录模块

TBD



## 特性要求

### 入参模块

argparse

### 配置可读模块

configparser

### 多线程下载

### 异步处理






## 函数说明

### 选择器：MethodSelector

> TBD 同时改造成支持命令行参数化输入

### 设置用户：setuid

> TBD 改造成使用@property

### 读取html源码：getcontent

> utf-8编码

### 设置页码范围：pagerange

> 如，喜欢页中文章较多，可以通过此处定义下载范围

### 尾页找寻：tailpage

> 通过读取某预览页，如喜欢页，获取最后一页

### 生成当页所有文章详情链接：detaillist

> 通过读取某预览页，如喜欢页，

### 文章详情页解析：parsedetail

> 

### 解析详情页中json格式：getjnfo

>

### 图片保存：saveimg

>

### 下载器：download

> 

### 保存流程：processsave

> 

### 计算文章总数量：processliketail

> 

### 进度条:processbar

> 



### 写入文章详情表：to_bcy_detail_post

> 



### 写入详情用户信息表：to_bcy_detail_user

> 



### 连接并写入mysql:insert_to_mysql

> 

## mysql

文章页详情信息存储

```mysql
CREATE TABLE `bcy_detail_post` (
  `item_id` varchar(20) NOT NULL,
  `uid` int(10) unsigned NOT NULL,
  `plain` varchar(500) DEFAULT NULL,
  `multi_original_path` json DEFAULT NULL COMMENT 'mid,original_path',
  `work` varchar(20) DEFAULT NULL,
  `wid` mediumint(8) unsigned DEFAULT NULL,
  `like_count` int(10) unsigned DEFAULT '0',
  `reply_count` smallint(5) unsigned DEFAULT '0',
  `share_count` smallint(5) unsigned DEFAULT '0',
  PRIMARY KEY (`item_id`),
  KEY `IDX_BCY_ITEMID` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```



文章页用户信息存储

```mysql
CREATE TABLE `bcy_detail_user` (
  `uid` int(10) unsigned NOT NULL,
  `uname` varchar(30) NOT NULL,
  `sex` enum('0','1') DEFAULT NULL,
  `self_intro` varchar(300) DEFAULT NULL,
  `following` int(10) unsigned DEFAULT '0',
  `follower` int(10) unsigned DEFAULT '0',
  `utags` json DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```



半次元图片路径存储

```mysql\
CREATE TABLE `bcy_img` (
  `mid` varchar(10) NOT NULL,
  `original_path` varchar(100) DEFAULT NULL,
  `local_path` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```



代理池

```mysql
CREATE TABLE `proxies_pool` (
  `ip` varchar(16) NOT NULL,
  `port` smallint(5) unsigned NOT NULL,
  `protocol` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`ip`,`port`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

