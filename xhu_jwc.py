# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

__author__ = 'quanchimi'
__version = '开发中'

# 没事重构下


class XHU_JWC:
    # 初始化方法 构造headers,data
    def __init__(self):
        self.s = requests.session()
        self.jwc_url = 'http://jwc.xhu.edu.cn/default6.aspx'
        self.xh= '312012080609303'

        # headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36',
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Accept-Language': 'zh-CN,zh;q=0.8',
            # 'Content-Length': '447',
            # 'Content-Type':'application/x-www-form-urlencoded',
            # 'Host':'jwc.xhu.edu.cn',
            # 'Origin':'http://jwc.xhu.edu.cn',
            # 'Referer':'http://jwc.xhu.edu.cn/default6.aspx',
            # 'Connection':'keep-alive',
        }
        # data
        self.data = {
            ###
            # __VIEWSTATE :登陆所需要的必要参数之一，先get一次登陆界面，从登陆界面中获取
            # xh : 学号
            # txtMm : 密码
            ###

            '__VIEWSTATE': self.getData(self.jwc_url,self.s),
            # 'tbtns':'',
            # 'tnameXw': 'yhdl',
            # 'tbtnsXw': 'yhdl|xwxsdl',
            # 还没想好怎么做交互
            'txtYhm': self.xh,
            # 'txtXm':'',
            'txtMm': 'qq142857',
            'rblJs': '学生',
            'btnDl': '登陆'
        }

    # 访问一次页面，获得必要的参数
    def getData(self,jwc_url,s):

        get_result = s.get(self.jwc_url,headers=self.headers)
        soup_login = BeautifulSoup(get_result.text,"html5lib")
        # 嗯，就是__VIEWSTATE
        login_VIEWSTATE = soup_login.body.form.input['value']

        # print(login_VIEWSTATE)
        return login_VIEWSTATE

    # 登陆,同时获取下一步所必要的数据
    def login(self, jwc_url, s):
        login_result = s.post(self.jwc_url, headers=self.headers, data=self.data)
        xs_main_url = 'http://jwc.xhu.edu.cn/xs_main.aspx?xh=' + str(self.xh)
        main_page_headers ={
            'Referer':xs_main_url
        }
        print(login_result.text)
        return login_result.text, main_page_headers

    # def cjcx(self,s,main_page_headers):
    #     cjcx_params = {
    #         'xh' : self.xh,
    #         'xm' : '权驰敉',
    #         'gnmkdm' :'N121605'
    #     }
    #     cjcx_url = 'http://jwc.xhu.edu.cn/xscjcx.aspx?'
    #     cjcx_page = s.get(cjcx_url, headers=main_page_headers, params=cjcx_params)
    #     print(cjcx_page.text)
    #     return cjcx_page.text


    def start(self):
        self.getData(self.jwc_url, self.s)
        self.login(self.jwc_url, self.s)
        # self.cjcx(self,self.s,)

a = XHU_JWC()
a.start()



