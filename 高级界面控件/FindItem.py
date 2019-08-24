# -*- coding:utf-8 -*-
# Time : 2019/08/24 上午 11:06 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : FindItem.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 示例2")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(600, 800)
        conLayout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(30)
        tableWidget.setColumnCount(4)
        conLayout.addWidget(tableWidget)
        for i in range(30):
            for j in range(4):
                itemContent = '(%d, %d)' % (i, j)
                tableWidget.setItem(i, j, QTableWidgetItem(itemContent))
        self.setLayout(conLayout)
        # 遍历表格查询对应项
        text = "(10, 1)"
        items = tableWidget.findItems(text, Qt.MatchExactly)
        item = items[0]
        # 选中单元格
        item.setSelected(True)
        # 设置单元格的背景色为红色
        item.setForeground(QBrush(QColor(255, 0, 0)))
        row = item.row()
        # 通过鼠标滚轮定位，快速定位到 11 行
        tableWidget.verticalScrollBar().setSliderPosition(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())