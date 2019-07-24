# !/usr/bin/env python3.7
# encoding: utf-8
# Time : 2019/6/23 17:23 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : CallMainWin01.py.py 
# @software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from 菜单栏和工具栏.MainWin01 import Ui_MainWindow


class MyMainWin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWin, self).__init__(parent)
        self.setupUi(self)
        # 菜单的点击事件，当点击关闭菜单时连接槽函数 close()
        self.fileCloseAction.triggered.connect(self.close)
        # 当点击打开菜单时连接槽函数 openMsg()
        self.fileOpenAction.triggered.connect(self.openMsg)

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "D:/", "All Files (*);;Text Files (*.txt)")
        # 在状态栏显示文件夹地址
        self.statusbar.showMessage(file)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWin()
    win.show()
    sys.exit(app.exec_())
