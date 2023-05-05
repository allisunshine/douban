# -*- coding = utf-8 -*-
# @Time : 2023/5/4 23:03
# @Author : maxiaoyun
# @File : testBs4.py
# @Software : PyCharm

"""
BeautifulSoup4将复杂html文档转换成一个复杂的树形结构，每个节点都是Python对象，所有对象可以归纳为4种
- Tag 标签及其内容（第一个）
- NavigableString
- BeautifulSoup
- Comment
"""
import re

from bs4 import BeautifulSoup

# tag
file = open("./baidu.html", "rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")


# print(bs.title)
# print(bs.a)

# NavigableString标签里的内容
# print(bs.title.string)
# print(bs.a.attrs)
# print(bs.name)
# print(type(bs))

# Comment注释
# print(type(bs.a.string))


# -------------------------------------------
# 文档的遍历
# print(bs.head.contents)
# print(bs.head.contents[1])

# 文档的搜索
# 完全匹配
# t_list = bs.find_all("a")
# t_list = bs.find_all("head")

# 正则表达式搜索：使用search（）匹配
# t_list = bs.find_all(re.compile("a"))

# 方法：传入一个函数，根据函数的要求搜索
def name_is_exists(tag):
    return tag.has_attr("name")


# t_list = bs.find_all(name_is_exists)

# kwargs 参数
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_=True)
# t_list = bs.find_all(href="http://news.baidu.com")

# 文本参数
# t_list = bs.find_all(string = re.compile("\d"))

# css选择器
t_list = bs.select("title")  # 通过标签查找
t_list = bs.select(".mnav")  # 通过类名查找
t_list = bs.select("#u1")  # 通过id查找
t_list = bs.select("a[class='bri']")  # 通过属性查找
t_list = bs.select("head > title")  # 通过子标签查找
t_list = bs.select(".mnav ~ .bri")  # 通过兄弟查找
print(t_list[0].get_text())

for item in t_list:
    print(item)
