# -*- coding:utf-8 -*-
# Time : 2019/10/01 上午 9:52 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : test.py 
# @software: PyCharm

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

if __name__ == "__main__":
    db = QSqlDatabase.addDatabase("QODBC")
    db.setHostName("192.168.3.192")
    db.setDatabaseName("db_2012")
    db.setUserName("Sa")
    db.setPassword("953")
    dbConnect = db.open()
    if dbConnect:
        query = QSqlQuery()
        query.exec_("select * from Student")
        db.close()
