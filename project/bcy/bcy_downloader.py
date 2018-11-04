#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from urllib.parse import urlencode
from urllib.parse import urljoin
from datetime import datetime
from requests import codes
import os
# from hashlib import md5
# from multiprocessing.pool import Pool
from bs4 import BeautifulSoup
import re
import json

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
    def __init__(self,**info):
        """
        [initial]
        param bcyurl:base website_url for urljoin.
        param headers:for requests incase of prevented by bcy.net.
        """
        self.bcyurl='https://bcy.net/'
        self.headers={
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

    def Method_Selector(self,Method=1):
        """
        param Methods:Options for instance
        1: Get pics from "喜欢"(like) page.
        2: Get pics from "原作/标签"(original or labels) page.
        3: Get pics from the Top List. 
        4: Get the videos.
        5: Get the novels.
        6: Get "comment" from an article
        """
        self.Method=Method
        if not self.set_uid :
            import random
            self.set_uid(int(random.random()*2000000))
        if self.Method == 1:
            self.url_join='/u/{0}/like'.format(self.uid)
        elif self.Method == 2:
            self.url_join='/u/{0}/like/circle'.format(self.uid)
        elif self.Method == 3:
            self.url_join='/coser'
        elif self.Method == 4:
            self.url_join='/video'
        elif self.Method == 5:
            self.url_join='/novel'
        elif self.Method == 6:
            self.get_comment()
        else :
            print("Check the Method Please!")
        self.url=urljoin(self.bcyurl,self.url_join)



    def set_uid(self,uid):
        """
        param uid: the user_id of bcy.net
        """
        self.uid=uid


    def get_content(self,*url):
        """
        return article_list according to methods.
        """
        if self.Method:
            url=self.url
        try:
            rg=requests.get(url,headers=self.headers)
            if rg.status_code == codes.ok:
                return rg.text
        except requests.ConnectionError:
            return None    

    def get_pages(self,content,**pages):
        """
        before implement func detail_list,
        we can set the range of page we need to process,
        or process all the pages
        param **pages: dict for page begin and end,eg.begin=1,end=2
        eg.
            pages={'begin':1,'end':2} 
        return list of pages
        """     
        
        try:
            #需要重新设定，是否使用像numpy的接收元组(1,2)作为参数
            begin_page = pages['begin']
            end_page = pages['end']
        except NameError :
            soup = BeautifulSoup(content,'lxml')
            begin_page = 1
            #这里也有可能某些用户没有Like内容，需要捕获异常，不过测试了下，为空不影响页面使用，但可能影响下面的循环range
            end_page = soup.find_all(name='li',attrs={'class':'pager__item js-nologinLink'},text='尾页')    
            end_page = end_page[0].a.get('href')
            end_page = re.search('p=(\d+)',end_page)
            end_page = end_page.groups()[0]
        finally:
            #是否使用yield返回每个页面，可以考虑
            for page_num in ranges(int(begin_page)+1,int(end_page)+1):
                url=urljoin(self.bcyurl,'{0}?&p={1}'.format(self.url_join,page_num))
                content=self.get_content(url)
                self.detail_list(content)



    def detail_list(self, content):
        """
        generator detail_article_list 
        """
        soup = BeautifulSoup(content,'lxml')
        #可以格式化或不格式化，没影响
        soup.prettify()
        #Bs_list形式存储所有找到的图文href
        # like_tags=soup.find_all(name='ul',attrs={'class':'l-clearfix gridList smallCards'})
        like_tags=soup.find_all(name='a',attrs={'class':'db posr ovf'})
        for tag in like_tags:
            yield {
                tag.li.a.attrs['title']:tag.li.a.attrs['href']
            }
            
    def parse_detail(self,**kwargs):
        """
        Get the pics from detail pages
        return article with img info as json
        """
        #直接输入page=完整连接，或者href相对连接自动拼接
        detail_page='https://bcy.net/item/detail/6488041845753405198'
        rgd = requests.get(detail_page,headers=self.headers)
        soupd = BeautifulSoup(rgd.text,'lxml')
        soupd.article.find_all(attrs={'class':'img-wrap-inner'})
        soupd.article.find_all(attrs={'class':'content'})
        soupd.article.find_all(attrs={'class':'album'})
        return article_json

    def save_img(self,article_json):
        """
        param uname: classify images by uname_dir #但是应该注意昵称的特殊符号处理
        param img_path: get from article_json for download.
        """
        from urllib.requests import urlretrieve
        dirname=pathlist
        os.makedirs(dirname,exist_ok=True)
        pathlist
        urlretrieve('https://img-bcy-qn.pstatp.com/coser/58850/post/c0c4p/84d31100c88511e7b1be05ee2d688961.jpg','1.jpg')
        
    def log():
        pass
    def usage():
        """
        step1:
        bcy=BCY_DownLoader()
        step2:
        bcy.set_uid(605084)
        step3:
        bcy.Method_Selector(1)
        step4: ignore this param_url if exists step3
        like_content=bcy.get_content(url)
        step5:
        detail_list
        """

        



def main():
    bcy=BCY_DownLoader()
    bcy.set_uid(605084)

if __name__ == '__main__':
    main()