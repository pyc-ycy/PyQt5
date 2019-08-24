# -*- coding:utf-8 -*-
# Time : 2019/08/23 上午 8:44 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : QTableWidgetTest.py 
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
        self.setWindowTitle("QTableWidget 例子")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(400, 300)
        conLayout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(6)
        tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget)
        tableWidget.setHorizontalHeaderLabels(['姓名  ', '性别', '体重(kg)'])
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
        comBox = QComboBox()
        comBox.addItem("男")
        comBox.addItem("女")
        comBox.setStyleSheet("QComboBox{margin:3px};")
        tableWidget.setCellWidget(0, 1, comBox)
        searchBtn = QPushButton("修改")
        searchBtn.setDown(True)
        searchBtn.setStyleSheet("QPushButton{margin:3px};")
        tableWidget.setCellWidget(0, 2, searchBtn)
        newItem = QTableWidgetItem("雅男")
        tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem('女')
        tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('98')
        tableWidget.setItem(0, 2, newItem)
        item1 = QTableWidgetItem('彭友聪')
        item2 = QTableWidgetItem('男')
        item3 = QTableWidgetItem('139')
        tableWidget.setItem(3, 0, item1)
        tableWidget.setItem(3, 1, item2)
        tableWidget.setItem(3, 2, item3)
        self.setLayout(conLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())
