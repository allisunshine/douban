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

"""
.*?和.*的区别：
没有?表示贪婪模式。比如a.*b，它将会匹配最长的以a开始，以b结束的字符串。如果用它来搜索aabab的话，它会匹配整个字符串aabab
有?表示非贪婪模式，匹配最短的。比如a.*?b，以a开始，以b结束的字符串。如果把它应用于aabab的话，它会匹配aab（第一到第三个字符）和ab（第四到第五个字符）
"""
# 影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片的链接
findImgSrc = re.compile(r'<img.*?src="(.*?)"', re.S)  # re.S忽略换行符
# 影片的片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 找到评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取网页
    datalist = getData(baseurl)
    # excel保存数据
    # savepath = "豆瓣电影Top250.xls"
    # saveData(datalist, savepath)

    # db保存数据
    dbpath = "movie.db"
    save2DB(datalist, dbpath)


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
        # print(html)
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
        html = askURL(url)
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            # 保存一部电影的所有信息
            data = []
            item = str(item)
            # 影片详情的链接
            link = re.findall(findLink, item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
                ctitle = titles[0]
                otitle = titles[1].replace("/", "")
                data.append(ctitle)
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")  # 外国名留空
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉空格
            datalist.append(data)
    return datalist


# 保存数据
def saveData(datalist, savepath):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, len(col)):
        worksheet.write(0, i, col[i])
    for i in range(0, len(datalist)):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, len(data)):
            worksheet.write(i + 1, j, data[j])
    workbook.save(savepath)


# 保存db
def save2DB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql = """
                insert into movie250 (info_link,pic_link,cname,ename,score,rated,instroduction,info)
                values (%s)
        """ % ",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


# 创建数据库
def init_db(dbpath):
    sql = """
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        instroduction text,
        info text
        );
    """
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    #
    main()
    # init_db("movietest.db")
    # print("db successful")
