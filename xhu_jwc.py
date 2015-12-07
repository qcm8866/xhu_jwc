# -*- coding:utf-8 -*-
__author__ = 'quanchimi'
import requests
from  bs4 import BeautifulSoup
# 没事重构下
class XHU_JWC:
    #初始化方法，定义一些变量
    def __init__(self):
        xh= '312012080609303'
        headers = {
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
        data = {
            # '__VIEWSTATE': login_VIEWSTATE,
            # 'tbtns':'',
            # 'tnameXw': 'yhdl',
            # 'tbtnsXw': 'yhdl|xwxsdl',
            'txtYhm': xh,
            # 'txtXm':'',
            'txtMm': 'qq142857',
            'rblJs': '学生',
            'btnDl': '登陆'
        }

    def getURL(self):
        jwc_url = 'http://jwc.xhu.edu.cn/default6.aspx'
        s=requests.session()
        get_result = s.get(jwc_url)
        print(get_result.text)
        return get_result.text


a = XHU_JWC()
a.getURL()



