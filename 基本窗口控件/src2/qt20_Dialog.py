# -*- coding:utf-8 -*-
# Time : 2019/08/16 上午 10:52 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt20_Dialog.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pymysql
import pandas.io.sql as sql


class DialogDemo(QMainWindow):
    def __init__(self, parent=None):
        super(DialogDemo, self).__init__(parent)
        self.setWindowTitle("Dialog 例子")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(350, 300)

        self.btn = QPushButton(self)
        self.btn.setText("弹出对话框")
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.showDialog)

        self.btn1 = QPushButton("连接数据库查询")
        self.btn1.move(80, 80)
        self.btn1.clicked.connect(self.conn)

        self.txid = QTextEdit()
        self.txid.move(100, 100)

    def showDialog(self):
        dialog = QDialog()
        btn = QPushButton("ok", dialog)
        btn.move(50, 50)
        dialog.setWindowTitle("Dialog")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    def conn(self):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root19537',
            db='test',
            charset='utf8'
        )
        if conn:
            print('成功连接数据库！！！')
            s = str.format("select * from tb_user where username like '{}'", "ycy")
            result = sql.read_sql_query(s, conn)
            self.txid.setPlaceholderText(result)
            conn.close()
        else:
            print('数据库连接失败！！！！')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = DialogDemo()
    demo.show()
    sys.exit(app.exec_())
