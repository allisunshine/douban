# -*- coding = utf-8 -*-
# @Time : 2023/5/3 18:52
# @Author : maxiaoyun
# @File : testUrllib.py
# @Software : PyCharm
import urllib.request
import urllib.parse
import ssl

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

# get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))

# post请求
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(response.read().decode("utf-8"))

# 超时
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=1)
#     print(response.read().decode("utf-8"))
# except TimeoutError as e:
#     print("超时了")

# response = urllib.request.urlopen("http://httpbin.org/get")
# print(response.status)
# print(response.getheaders())
# print(response.getheader("Server"))

# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({"name": "buer"}), encoding="utf-8")
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
