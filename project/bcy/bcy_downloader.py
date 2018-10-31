#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
分析方案:

登录https://bcy.net

方案选择器：1 我的喜欢  2 原作/标签 3 获取评论 4 指定用户下图片

进入个人主页https://bcy.net/u/605084

选择我的喜欢https://bcy.net/u/605084/like

获取内容分类下的图文原址作为list

登录list[i] https://bcy.net/item/detail/6581722283805507847

获取article标签下所有大图 <div class="img-wrap-inner"><img src="https://img-bcy-qn.pstatp.com/user/30172/item/web/179no/9314ae308f2811e89ada1b5c766b8a41.jpg/w650"></div>

将获取的src地址去掉w650后下载，建立所有article对应的title目录<a class="cut" href="/u/30172" title="洛霁无">洛霁无</a>

考虑分布式下载
"""

import requests
from urllib.parse import urlencode
from requests import codes
import os
# from hashlib import md5
# from multiprocessing.pool import Pool
import random
from bs4 import BeautifulSoup
import re

class BCY_DownLoader(obejct):
    #The Strategy of Bcy_downloader
    def __init__(self,Strategy=1,uid):
        self.Strategy=Strategy
        # try:
        #     self.set_uid(uid)
        # except AttributeError:
        self.set_uid(int(random.random()*2000000))
        self.headers={
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

    def Strategy_Selector(self):
        """
        choose Strategy for 3 methods
        1: get "like"
        2: get "original or labels"
        3: get "comment"
        """
        if self.Strategy == 1:
            self.url='https://bcy.net/u/'+self.uid+'/like'
        if self.Strategy == 2:
            pass
        if self.Strategy == 3:
            pass


    def set_uid(self,uid):
        """
        set the user_id
        """
        self.uid=uid

    def get_page(self,url):
        """
        return html_content of Method
        """
        try:
            rg=requests.get(url,headers=self.headers)
            if rg.status_code == codes.ok:
                return rg.text
        except requests.ConnectionError:
            return None                

    def parse_like(self, page):
        #如果需要遍历每页，则需要https://bcy.net/u/605084/like?&p=21，循环parse_html，并设定try
        soup = BeautifulSoup(page,'lxml')
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
        #直接输入page=完整连接，或者href相对连接自动拼接
        detail_page='https://bcy.net/item/detail/6488041845753405198'
        rgd = requests.get(detail_page,headers=self.headers)
        soupd = BeautifulSoup(rgd.text,'lxml')
        soupd.article.find_all(attrs={'class':'img-wrap-inner'})
        soupd.article.find_all(attrs={'class':'content'})
        soupd.article.find_all(attrs={'class':'album'})


        


        
from __main__ import BCY_DownLoader.parse_content
page='https://bcy.net/u/605084/like'
BCY_DownLoader.parse_content(page)


ipython

import requests
from urllib.parse import urlencode
from requests import codes
import os
import random
from bs4 import BeautifulSoup
import re

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
url='https://bcy.net/u/605084/like'
rg=requests.get(url,headers=headers)
soup = BeautifulSoup(rg.text,'lxml')
detail_page='https://bcy.net/item/detail/6488041845753405198'
rgd=requests.get(detail_page,headers=headers)
#中文编码
rgd.encoding='utf-8'
soupd = BeautifulSoup(rgd.text,'lxml')

#发现图片其实在soupd.find_all(name='script')中的某个window.__ssr_data = JSON.parse

json_img=soupd.find_all(name='script',text=re.compile('JSON.parse(.*);(.*)'))

json_img=re.findall('JSON.parse\("(.*)"\);',str(json_img))
import json
str_j=re.sub('\\\\','\\',json_img[0])
jd=json.loads(str_j)

soup.find_all(name='a',attrs={'class':'db posr ovf'})[0].attrs['title']
soup.find_all(name='a',attrs={'class':'db posr ovf'})[0].attrs['href']
soup.find_all(name='ul',attrs={'class':'l-clearfix gridList smallCards'})
soup.find_all(name='ul',attrs={'class':'l-clearfix gridList smallCards'})[0].li.a.attrs['href']
