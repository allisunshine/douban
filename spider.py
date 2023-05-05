# -*- coding = utf-8 -*-
# @Time : 2023/5/3 17:26
# @Author : maxiaoyun
# @File : spider.py
# @Software : PyCharm

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib  # 制定url，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行sqlite数据库操作
import urllib.request
import ssl

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取网页
    datalist = getData(baseurl)
    # 保存数据
    # savepath = ".\\豆瓣电影Top250.xsl"
    # saveData(savepath)


# 得到一个指定URL网页的内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调取十次，一次25条，一共250条
        url = baseurl + str(i * 25)
        # 逐一解析数据
        html = askURL(url)

    return datalist


# 保存数据
def saveData(savepath):
    print("...")


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
