# -*- coding:utf-8 -*-
# Time : 2019/10/01 上午 10:07 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : dbOption01.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *


def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./db/database.db')

    if not db.open():
        QMessageBox.critical(None, ("无法打开数据库连接"), ("无法建立到数据库的连接，这个例子需要SQLite支持"), QMessageBox.Cancel)
        return False

    query = QSqlQuery()
    query.exec_("create table people(id int primary key, name varchar(20), address varchar(30))")
    query.exec_("insert into people values(1, 'zhangsan', 'beijing')")
    query.exec_("insert into people values(2, 'wangwu', 'shanghai')")
    query.exec_("insert into people values(3, 'lisi', 'guangzhou')")
    query.exec_("insert into people values(4, 'zhaoliu', 'kunming')")
    db.close()
    return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    createDB()
    sys.exit(app.exec_())
