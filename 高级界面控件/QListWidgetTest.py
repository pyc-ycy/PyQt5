# -*- coding:utf-8 -*-
# Time : 2019/08/25 下午 5:07 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : QListWidgetTest.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ListWidget(QListWidget):
    def clicked(self, item):
        QMessageBox.information(self, "ListWidget", "你选择了：" + item.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    listWidget = ListWidget()
    listWidget.resize(300, 120)
    listWidget.addItem("Item 1")
    listWidget.addItem("Item 2")
    listWidget.addItem("Item 3")
    listWidget.addItem("Item 4")
    listWidget.setWindowTitle("QListWidget 例子")
    listWidget.setWindowIcon(QIcon("./images/Python2.ico"))
    listWidget.itemClicked.connect(listWidget.clicked)
    listWidget.show()
    sys.exit(app.exec_())