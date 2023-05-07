# -*- coding = utf-8 -*-
# @Time : 2023/5/7 16:52
# @Author : maxiaoyun
# @File : testSqlite.py
# @Software : PyCharm

import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()
# sql = """
#     create table company
#         (id int primary key not null ,
#         name text not null ,
#         age int not null ,
#         address char(50),
#         salary real
#         );
# """

# sql = """
#     insert into company (id,name,age,address,salary)
#     values (1,"张三",18,"cehngdu",8000)
# """
sql = "select * from company"
cursor = c.execute(sql)
for row in cursor:
    print(row)
conn.commit()
conn.close()
print("select database successfully")
