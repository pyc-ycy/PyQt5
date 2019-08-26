# -*- coding:utf-8 -*-
# Time : 2019/08/26 下午 3:36 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : treeViewTest.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Window 系统提供的模式
    model = QDirModel()
    # 创建一个 QTreeView 控件
    tree = QTreeView()
    # 为控件添加模式
    tree.setModel(model)
    tree.setWindowTitle("QTreeView 例子")
    tree.setWindowIcon(QIcon("./images/Python2.ico"))
    tree.resize(640, 480)
    tree.show()
    sys,exit(app.exec_())