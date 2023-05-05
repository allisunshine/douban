# -*- coding = utf-8 -*-
# @Time : 2023/5/5 00:14
# @Author : maxiaoyun
# @File : testRe.py
# @Software : PyCharm
import re

# 正则表达式
# pat = re.compile("AA")
# m = pat.search("ABCAA")

# m = re.search("asd", "Aasd")
m = re.findall("[A-Z]", "ADsdfDAF")
m = re.findall("[A-Z]+", "ADsdfDAF")
m = re.sub("a", "A", r"asxzvdsfa")
# 建议加r，防止转义字符被转译
a = r"\aabd\'"
print(a)
print(m)
