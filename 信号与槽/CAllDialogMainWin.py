# -*- coding:utf-8 -*-
# Time : 2019/09/16 下午 9:01 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : CAllDialogMainWin.py 
# @software: PyCharm


from 信号与槽.DateDialog import DateDialog
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.resize(400, 90)
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setWindowTitle("窗口传递数据")
        self.lineEdit = QLineEdit(self)
        self.button1 = QPushButton("弹出对话框1")
        self.button1.clicked.connect(self.onButton1Click)
        self.button2 = QPushButton('弹出对话框2')
        self.button2.clicked.connect(self.onButton2Click)
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)
        self.setLayout(gridLayout)

    def onButton1Click(self):
        dialog = DateDialog(self)
        result = dialog.exec_()
        date = dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        print('\n 日期对话框的返回值')
        print('date=%s' % str(date.date()))
        print('time=%s' % str(date.time()))
        print('result=%s' % result)
        dialog.destroy()

    def onButton2Click(self):
        date, time, result = DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        print('\n 日期对话框的返回值')
        print('date=%s' % str(date))
        print('time=%s' % str(date))
        print('result=%s' % result)
        if result == QDialog.Accepted:
            print('点击确认按钮')
        else:
            print('点击取消按钮')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWin()
    form.show()
    sys.exit(app.exec_())
