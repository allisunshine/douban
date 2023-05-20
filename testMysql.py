# -*- coding = utf-8 -*-
# @Time : 2023/5/21 01:46
# @Author : maxiaoyun
# @File : testMysql.py
# @Software : PyCharm

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# 创建引擎
engine = create_engine('mysql+mysqlconnector://root@127.0.0.1:3306/python_project')

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)


def insert():
    # 插入数据
    data = Test(name='John Doe')
    session.add(data)
    session.commit()


def query():
    # 查询数据
    result = session.query(Test).all()
    for item in result:
        print(item.id, item.name)
    return result


def update():
    # 修改数据
    data = query()[0]
    data.name = 'Jane Smith'
    session.commit()
    print(data)


def delete():
    data = query()[0]
    # 删除数据
    session.delete(data)
    session.commit()


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    update()
