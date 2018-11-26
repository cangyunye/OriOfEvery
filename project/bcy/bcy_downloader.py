#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from urllib.parse import urlencode
from urllib.parse import urljoin
from urllib.request import urlretrieve
from urllib.error import ContentTooShortError
from requests import codes
# from hashlib import md5
# from multiprocessing.pool import Pool
from bs4 import BeautifulSoup
import re
import os
import random
from datetime import datetime as dt
from time import sleep
import functools
from tqdm import tqdm
# import types

__version__bcy__ = '1.0.0'

__bibtex__ = r"""@Article{cangyunye:2018,
  Author    = {cangyunye},
  Title     = {BcyDownLoader:collector for bcy.net},
  abstract  = {.},
  publisher = {cangyunye},
  year      = 2018
}"""

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("{}:Call {}".format(dt.now(),func.__name__))
        return func(*args,**kw)
    return wrapper

        
def delay(func):
    """
    random time for sleep as decorator
    """
    def wrapper(*args,**kw):
        # sleep(random.sample([t for t in range(3)],1)) 
        delaytime = random.uniform(0,3)
        sleep(delaytime)
        print('delaytime:{}'.format(delaytime))
        return func(*args,**kw)
    return wrapper
    

class BcyDownLoader():
    """
    Collection the pictures from bcy.net
    There are optional methods for download pics.
    methods: referenced by Method_Selector

    """

    def __init__(self):
        """
        [initial]
        param:
            bcyurl:base url of banciyuan.
            detailurl:basesite of detail article
            headers:for requests incase of prevented by bcy.net.
            # batch:count of download every time.
        """
        self.bcyurl = 'https://bcy.net/'
        self.detailurl = 'https://bcy.net/item/detail/'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
  
    @log
    def Method_Selector(self, Method=1,*prange):
        """
        params:
            Methods:
            Options for instance
            1: Get pics from "喜欢"(like) page.
            2: Get pics from "原作/标签"(original or labels) page.
            3: Get pics from the Top List. 
            4: Get the videos.
            5: Get the novels.
            6: Get "comment" from an articlec
        return:
            self.url
        """
        self.Method = Method
        if not self.set_uid: 
            self.set_uid(int(random.random()*2000000))
        if self.Method == 1:
            self.url_join = '/u/{0}/like'.format(self.uid)
            self.url = urljoin(self.bcyurl, self.url_join)
            likepg = self.get_content(self.url) #获取"like"页html代码
            likepg_list = self.page_range(likepg,prange[0],prange[1]) #分析并输出选择的"like"页码范围
            for page in likepg_list:
                #获取like"页html代码
                like = self.get_content(page) 
                # print('like',like)
                #提取当前"like"页所有detail页码
                likedt_list = self.detail_list(like)
                # print('likedt_list',likedt_list)
                #下载所有detail页内图片
                self.parse_detail(likedt_list)
        elif self.Method == 2:
            self.url_join = '/u/{0}/like/circle'.format(self.uid)
        elif self.Method == 3:
            self.url_join = '/coser'
        elif self.Method == 4:
            self.url_join = '/video'
        elif self.Method == 5:
            self.url_join = '/novel'
        elif self.Method == 6:
            self.get_comment()
        else:
            print("Check the Method Please!")
        self.url = urljoin(self.bcyurl, self.url_join)
        return self.url
    @log
    def set_uid(self, uid):
        """
        param: 
            uid: the user_id of bcy.net
        """
        self.uid = uid
    @log
    def get_content(self, url):
        """
        params:
            url
        return:
            html source code.
        """
        try:
            rg = requests.get(url, headers=self.headers)
            if rg.status_code == codes.ok:
                rg.encoding = 'utf-8'
                return rg.text
        except requests.ConnectionError:
            return None
    @log
    def page_range(self,content,*prange):
        """
        before implement func detail_list,
        we can set the range of page we need to process,
        or process all the pages
        params:
            *prange: tuple for page begin to end.
            eg.begin=1,end=20
            prange=(1,20)
        return list of like page range
        """
        if len(prange) == 2:
            begin_page,end_page = prange
        elif len(prange) == 1:
            begin_page = prange[0]
            end_page = self.tailpage(content)
        else :
            begin_page = 1
            end_page = self.tailpage(content)
        pages_list = []
        for page_num in range(int(begin_page), int(end_page)+1):
            pages_list.append(
                urljoin(self.bcyurl, '{0}?&p={1}'.format(self.url_join, page_num)))
        return pages_list

    @log    
    def tailpage(self,content) : 
        #判断尾页
        soup = BeautifulSoup(content, 'lxml')
        end_page = soup.find(
            name='li', attrs={'class': 'pager__item js-nologinLink'}, text='尾页')
        if end_page:
            end_page = end_page.a.get('href')
            end_page = re.search('p=(\d+)', end_page)
            end_page = end_page.groups()[0]
        else:
            end_page = 1
        return end_page

    @log
    def detail_list(self, content):
        """
        Generate detail_article_list 
        params:
            content: html code from detail_page
        return:
            dict['title']=href
        """
        soup = BeautifulSoup(content, 'lxml')
        soup.prettify()
        like_tags = soup.find_all(name='a', attrs={'class': 'db posr ovf'})
        detail_list = []
        for tag in like_tags:
            detail_list.append(urljoin(self.bcyurl, tag.attrs['href']))
        # print('detail_list\n',detail_list)
        # print(type(detail_list))
        return detail_list

    @log
    def parse_detail(self, detail_page=None,**detail):
        """    
        params:
            detail_page:pages of pics with articles
            **detail:{'dn':'6488041845753405198'}
            or {'dn1':'6488041845753405198','dn2':'6214365223982227214'}

        """
        if len(detail) > 0:
            for dn in detail.values():
                detail_page = urljoin(self.detailurl, dn)
        elif isinstance(detail_page,list): 
            for de_page in detail_page:
                print('de_page',de_page)
                self.parse_detail(de_page)
        elif isinstance(detail_page,str):
            pass
        else :
            raise ValueError('Correct detail page have not been input.')
        
        print("parsing page:{}".format(detail_page)) 
        if detail:
            detail_num = detail['dn']
        else:
            # detail_num = re.search('detail/(.*)?',detail_page).groups()[0]
            detail_num = detail_page.split('/')[-1]

        rgd = requests.get(detail_page, headers=self.headers)
        rgd.encoding = 'utf-8'
        soupd = BeautifulSoup(rgd.text, 'lxml')
        """
        Parse the info from Html.
        """
        import json
        json_img = soupd.find_all(
            name='script', text=re.compile('JSON.parse(.*);(.*)'))
        json_img = re.findall('JSON.parse\("(.*)"\);', str(json_img))
        str_j = eval("'{}'".format(json_img[0]))
        jd = json.loads(str_j)
        jd_multi = jd['detail']['post_data']['multi'] 
        jd_uid = jd['detail']['detail_user']['uid']
        jd_uname = jd['detail']['detail_user']['uname']
        """
        Save imgs.
        """
        img_list = []
        # print('jd_multi',jd_multi)
        for img_l in jd_multi:  
            img_list.append(img_l['path'].rstrip('/w650'))
        # print('img_list',img_list)
        self.save_img(img_list,ppath=jd_uname,cpath=detail_num)
        return None

    @log
    def save_img(self, imgurl,**path):
        """ 
            params：
                imgurl: img path ，Compatibility of list and str.
                **path: {'ppath':'','cpath':''}
        """
        
        rpath = os.getcwd()
        try:
            if len(path) == 2 :
                ppath = os.path.join(rpath,path['ppath'])
                cpath = os.path.join(ppath,path['cpath'])
            elif len(path) == 1:
                cpath = os.path.join(rpath,path['path'])
        except NameError:
            print("There isn't any path dict like {'ppath':'','cpath':''} or {'path':},\n tmppath is set as label of today")
            cpath == str(dt.today().date())
        if not os.path.exists(cpath):
            os.makedirs(cpath)
            print(cpath,'Directory created successfully')
        else:
            print('Directory is exist.')

        os.chdir(cpath) 

        if isinstance(imgurl,list):
            for pic in imgurl:
                try:
                    self.download(pic,filename=pic.split('/')[-1])
                except ValueError:
                    print('{} is not a valid path'.format(pic))
        elif isinstance(imgurl,str):
            try:
                self.download(imgurl,filename=imgurl.split('/')[-1])
            except ValueError:
                print('{} is not a valid path'.format(imgurl))
        else:
            print('{} is not exist or the value is wrong'.format(imgurl))
        
        os.chdir(rpath) #以防意外，先留下
        return None

    @delay
    def download(self,inputs,filename):
        print('Download {}'.format(inputs))
        if os.path.exists(filename):
            print('{} is exist.'.format(filename))
            return None
        try:
            urlretrieve(inputs,filename=filename)
            print('success.')
        except ContentTooShortError:
            print('Download failed!Retry at 5 sec later')
            sleep(5)
            try:
                urlretrieve(inputs,filename=filename)
                print('success.')
            except ContentTooShortError:
                return None
        
    def usage(self):
        """
        #step1:
        bcy=BcyDownLoader() #设置类实例
        #step2:
        bcy.set_uid(605084)  #设置用户ID
        #step3:
        bcy.Method_Selector(1)  #选择模式 1 定义为"喜欢"页
        #step4: ignore this param_url if exists step3 
        like_content=bcy.get_content(url) #获取页面所有预览页html代码,这里不应该为显性的函数,url为内部定义
        #step5:
        page_list=bcy.page_range(like_content,begin=1,end=2) #分析"喜欢"页面html代码，返回所有的图文地址页
        #step6:
        all_content=bcy.get_content(page_list) #对所有图文地址页返回html代码
        #step7:
        detail_list_all = parse_detail(all_content) #遍历所有页面，获取coser 的uid和图片列表
        for detail in all_content:
            detail_list_all.append(detail_list(detail))
        可能得改下思路，每次处理一个页面之后再用重复的流程处理下一个
        #step8:
        #根据coser的uid建目录
        #step9:
        #根据coser的uid下载图片
        #step10:
        #装饰器设置各种随机sleep时间
        #step11:
        装饰器或者logging记录日志
        #step12:
        进度条显示：图片大小tqdm
        """


def main():
    
    #指定用户的喜欢页批量下载
    bcy = BcyDownLoader()
    bcy.set_uid(605084)
    url = bcy.Method_Selector(1,20,27) #下载第25到第26页
    

    """
    #指定detail下载，可单独使用
    bcy = BcyDownLoader()
    bcy.parse_detail(dn='6578730940602777859') 
    """

if __name__ == '__main__':
    main()
