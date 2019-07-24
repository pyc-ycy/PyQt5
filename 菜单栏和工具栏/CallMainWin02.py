# -*- coding:utf-8 -*-
# Time : 2019/07/24 下午 7:45 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : CallMainWin02.py 
# @software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from 菜单栏和工具栏.childrenForm2 import Ui_ChildrenForm2
from 菜单栏和工具栏.MainForm02 import Ui_MainWin02


class MainForm(QMainWindow, Ui_MainWin02):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        # self.child = children()生成子窗口实例self.child
        self.child = ChildrenForm()

        # 菜单的点击事件，当点击关闭菜单时连接槽函数 close()
        self.fileCloseAction.triggered.connect(self.close)
        # 当点击打开菜单时连接槽函数 openMsg()
        self.fileOpenAction.triggered.connect(self.openMsg)
        # 单击添加窗体，子窗口会显示在主窗口的 MaingridLayout 中
        self.addWinAction.triggered.connect(self.childShow)

    # 添加子窗口
    def childShow(self):
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "D:/", "All Files (*);;Text Files (*.txt)")
        # 在状态栏显示文件夹地址
        self.statusbar.showMessage(file)


class ChildrenForm(QWidget, Ui_ChildrenForm2):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())