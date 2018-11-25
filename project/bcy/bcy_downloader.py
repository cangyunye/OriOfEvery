#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from urllib.parse import urlencode
from urllib.parse import urljoin
from requests import codes
# from hashlib import md5
# from multiprocessing.pool import Pool
from bs4 import BeautifulSoup
import re
import random
from datetime import datetim as dt
from time import sleep
import functools

__version__bcy__ = '1.0.0'

__bibtex__ = r"""@Article{cangyunye:2018,
  Author    = {cangyunye},
  Title     = {BCY_DownLoader:collector for bcy.net},
  abstract  = {.},
  publisher = {cangyunye},
  year      = 2018
}"""


class BCY_DownLoader(obejct):
    """
    Collection the pictures from bcy.net
    There are optional methods for download pics.
    methods: referenced by Method_Selector

    """

    def __init__(self, **info):
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
    def Method_Selector(self, Method=1):
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
    def get_content(self, **url):
        """
        params:
            *url:
        return:
            html source code of Bs4.
        return article_list according to methods.
        if instance(url,list) :
            for i in url:
                rg=requests.get(i,headers=self.headers)
                yield rg.text #######
        content=self.get_content(url)
        self.detail_list(content)
        """
        if isinstance(url, list):
            try:
                for i in url:
                    rg = requests.get(i, headers=self.headers)
                    if rg.status_code == codes.ok:
                        rg.encoding = 'utf-8'
                        yield rg.text
            except requests.ConnectionError:
                return None
        elif self.Method:
            url = self.url
            try:
                rg = requests.get(url, headers=self.headers)
                if rg.status_code == codes.ok:
                    rg.encoding = 'utf-8'
                    return rg.text
            except requests.ConnectionError:
                return None
    @log
    def page_range(self, content, **pages):
        """
        before implement func detail_list,
        we can set the range of page we need to process,
        or process all the pages
        params:
            **pages: dict for page begin and end,eg.begin=1,end=2
            eg.
            pages={'begin':1,'end':2} 
        return list of pages
        """

        try:
            # 可以考虑，是否使用类似numpy的接收元组(1,2)作为参数
            begin_page = pages['begin']
            end_page = pages['end']
        except NameError:
            soup = BeautifulSoup(content, 'lxml')
            begin_page = 1
            # 这里也有可能某些用户没有Like内容，影响后续range，需要设定空值=1
            end_page = soup.find(
                name='li', attrs={'class': 'pager__item js-nologinLink'}, text='尾页')
            if end_page:
                end_page = end_page.a.get('href')
                end_page = re.search('p=(\d+)', end_page)
                end_page = end_page.groups()[0]
            else:
                end_page = begin_page
        finally:
            # 可以考虑.是否使用yield返回每个页面
            pages_list = []
            if end_page == begin_page:
                pages_list.append = urljoin(
                    self.bcyurl, '{0}?&p={1}'.format(self.url_join, begin_page))
            else:
                for page_num in ranges(int(begin_page)+1, int(end_page)+1):
                    pages_list.append(
                        urljoin(self.bcyurl, '{0}?&p={1}'.format(self.url_join, page_num)))
        return pages_list
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
        # Bs_list形式存储所有找到的图文href
        # like_tags=soup.find_all(name='ul',attrs={'class':'l-clearfix gridList smallCards'})
        like_tags = soup.find_all(name='a', attrs={'class': 'db posr ovf'})
        for tag in like_tags:
            yield {
                tag.li.a.attrs['title']: tag.li.a.attrs['href']
            }
    @log
    def parse_detail(self, *detail_page,**detail):
        """    
        params:
            detail_page:pages of pics with articles
            **detail:{'dn'='6488041845753405198'}
        """
        import json
        # 直接输入page=完整连接，或者href相对连接自动拼接
        img_list = []
        if len(detail) > 0:
            detail_page = urljoin(self.detailurl, detail['dn']))
        elif isinstance(detail_page,list): 
            for de_page in detail_page:
                self.parse_detail(de_page)
        elif isinstance(detail_page,str):
            detail_page = urljoin(self.bcyurl, self.detailurl))
        else:
            print('Correct detail page have not been input.')
        detail_num = re.search('detail/(.*)?',detail_page).groups()[0]
        rgd = requests.get(detail_page, headers=self.headers)
        rgd.encoding = 'utf-8'
        soupd = BeautifulSoup(rgd.text, 'lxml')
        """
        Parse the info from Html.
        """
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
        for img_l in jd_multi:
            img_l['path'].rstrip('/w650')
            img_list.append(img_l)
        self.save_img(img_list,ppath=jd_uname,cpath=detail_num)
        return None

    @log
    def save_img(self, imgurl,**path):
        """ 
            params：
                imgurl: img path ，Compatibility of list and str.
                **path: {'ppath':'','cpath':''}
        """
        import os
        from urllib.request import urlretrieve
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
        if not os.path.exists(path['cpath']):
            os.makedirs(cpath)
            print(path['cpath'],'Directory created successfully')
        else:
            print('Directory is exist.')

        os.chdir(cpath) 

        if isinstance(imgurl,list):
            for pic in imgurl:
                try:
                    self.download(pic)
                except ValueError:
                    print('{} is not a valid path'.format(pic))
        elif isinstance(imgurl,str):
             try:
                self.download(imgurl)
            except ValueError:
                print('{} is not a valid path'.format(imgurl))
        else:
            print('{} is not exist or the value is wrong'.format(imgurl))
        
        os.chdir(rpath) #以防意外，先留下
        return None

    @delay
    def download(self,inputs):
        urlretrieve(inputs)

    def log(text=None):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("{}:Call {}".format(dt.now(),func.__name__))
            return func(*args,**kw)
        return wrapper

        
    def delay():
        """
        random time for sleep as decorator
        """
        # sleep(random.sample([t for t in range(3)],1)) 
        sleep(random.uniform(0,3)))

    def usage():
        """
        #step1:
        bcy=BCY_DownLoader() #设置类实例
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
        使用装饰器或者logging记录日志
        """


def main():
    bcy = BCY_DownLoader()
    bcy.set_uid(605084)
    url = bcy.Method_Selector(1)
    like_content = bcy.get_content(url)
    page_range(like_content)


if __name__ == '__main__':
    main()
