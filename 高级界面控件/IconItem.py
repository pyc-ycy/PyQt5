# -*- coding:utf-8 -*-
# Time : 2019/08/25 上午 8:44 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : IconItem.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("表格图片示例")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(1000, 900)
        conLayout = QHBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setColumnCount(3)
        tableWidget.setRowCount(5)

        tableWidget.setHorizontalHeaderLabels(['图片 1', '图片 2', '图片 3'])
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tableWidget.setIconSize(QSize(300, 200))
        # 让列宽与图片相同
        for i in range(3):
            tableWidget.setColumnWidth(i, 300)
        # 让行高与图片相同
        for i in range(5):
            tableWidget.setRowHeight(i, 200)

        for k in range(15):
            i = k / 3
            j = k % 3
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled)  # 单击表格时，图片被选中
            icon = QIcon(r'.\images\bao%d.png' % k)
            item.setIcon(QIcon(icon))
            print('e/icons/%d.png i=%d j=%d' % (k, i, j))
            tableWidget.setItem(i, j, item)

        conLayout.addWidget(tableWidget)
        self.setLayout(conLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Table()
    win.show()
    sys.exit(app.exec_())
