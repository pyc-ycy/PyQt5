# -*- coding:utf-8 -*-
# Time : 2019/08/23 上午 8:44 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : QTableWidgetTest.py 
# @software: PyCharm


import sys

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(400, 300)
        conLayout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(6)
        tableWidget.setColumnCount(4)
        conLayout.addWidget(tableWidget)
        tableWidget.setHorizontalHeaderLabels(['姓名  ', '性别', '体重(kg)', '背包'])
        # 合并居中
        # tableWidget.setSpan(2, 0, 3, 1)
        # 设置表头可伸缩模式
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置行表头
        # tableWidget.setVerticalHeaderLabels(['行 1', '行 2', '行 3', '行 4', '行 5', '行 6'])
        # 设置为只读模式
        # tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置行高列宽为内容适配
        # tableWidget.resizeColumnsToContents()
        # tableWidget.resizeRowsToContents()
        # 隐藏水平方向的表头
        # tableWidget.verticalHeader().setVisible(False)
        # 隐藏垂直方向表头
        # tableWidget.horizontalHeader().setVisible(False)
        # 往单元格中添加基本控件
        '''comBox = QComboBox()
        comBox.addItem("男")
        comBox.addItem("女")
        comBox.setStyleSheet("QComboBox{margin:3px};")
        tableWidget.setCellWidget(0, 1, comBox)
        searchBtn = QPushButton("修改")
        searchBtn.setDown(True)
        searchBtn.setStyleSheet("QPushButton{margin:3px};")
        tableWidget.setCellWidget(0, 2, searchBtn)'''
        newItem1 = QTableWidgetItem("雅男")
        newItem1.setForeground(QBrush(QColor(255, 0, 0)))
        tableWidget.setItem(0, 0, newItem1)
        newItem2 = QTableWidgetItem('女')
        newItem2.setForeground(QBrush(QColor(255, 150, 0)))
        tableWidget.setItem(0, 1, newItem2)
        newItem3 = QTableWidgetItem('98')
        newItem3.setForeground(QBrush(QColor(255, 150, 150)))
        tableWidget.setItem(0, 2, newItem3)
        newItem4 = QTableWidgetItem(QIcon("./images/bao1.png"), "背包")
        tableWidget.setItem(0, 3, newItem4)
        item1 = QTableWidgetItem('友聪')
        item1.setFont(QFont("Times", 12, QFont.Black))
        item2 = QTableWidgetItem('男')
        item2.setFont(QFont("Times", 12, QFont.Black))
        item3 = QTableWidgetItem('139')
        item3.setFont(QFont("Times", 12, QFont.Black))
        item4 = QTableWidgetItem('御承扬')
        item4.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        item5 = QTableWidgetItem('未知')
        item5.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        item6 = QTableWidgetItem('120')
        item6.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        tableWidget.setItem(1, 0, item1)
        tableWidget.setItem(1, 1, item2)
        tableWidget.setItem(1, 2, item3)
        tableWidget.setItem(2, 0, item4)
        tableWidget.setItem(2, 1, item5)
        tableWidget.setItem(2, 2, item6)
        # 设置是否显示分隔线
        # tableWidget.setShowGrid(False)
        # 设置垂直表头不显示
        tableWidget.verticalHeader().setVisible(False)
        tableWidget.sortItems(2, QtCore.Qt.DescendingOrder)
        self.setLayout(conLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())
