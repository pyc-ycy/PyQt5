# -*- coding:utf-8 -*-
# Time : 2019/08/25 上午 9:46 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : tblMenu.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.tableWidget = QTableWidget()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(500, 300)
        conLayout = QHBoxLayout()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(8)
        conLayout.addWidget(self.tableWidget)
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        newItem = QTableWidgetItem('友聪 ')
        self.tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('145')
        self.tableWidget.setItem(0, 2, newItem)
        newItem = QTableWidgetItem('雅男')
        self.tableWidget.setItem(1, 0, newItem)
        newItem = QTableWidgetItem('女')
        self.tableWidget.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('87')
        self.tableWidget.setItem(1, 2, newItem)
        # 允许右键产生菜单
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # 将右键菜单绑定到槽函数
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)
        self.setLayout(conLayout)

    def generateMenu(self, pos):
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()

        # 表格中只有两条有效数据，所以只在前两行支持右键弹出菜单
        if row_num < 2:
            menu = QMenu()
            item1 = menu.addAction(u"选项一")
            item2 = menu.addAction(u"选项二")
            item3 = menu.addAction(u"选项三")
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            if action == item1:
                print('您选择了选项一，当前记录行的内容是：', self.tableWidget.item(row_num, 0).text(),
                      self.tableWidget.item(row_num, 1).text(), self.tableWidget.item(row_num, 2).text())
            elif action == item2:
                print('您选择了选项二，当前记录行的内容是：', self.tableWidget.item(row_num, 0).text(),
                      self.tableWidget.item(row_num, 1).text(), self.tableWidget.item(row_num, 2).text())
            elif action == item3:
                print('您选择了选项三，当前记录行的内容是：', self.tableWidget.item(row_num, 0).text(),
                      self.tableWidget.item(row_num, 1).text(), self.tableWidget.item(row_num, 2).text())
            else:
                return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Table()
    win.show()
    sys.exit(app.exec_())
