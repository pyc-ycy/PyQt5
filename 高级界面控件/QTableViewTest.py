# -*- coding:utf-8 -*-
# Time : 2019/08/21 下午 8:09 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : QTableViewTest.py 
# @software: PyCharm


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Table(QWidget):
    def __init__(self, arg=None):
        super(Table, self).__init__(arg)
        self.setWindowTitle("QTableView 示例")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(500, 300);
        self.model = QStandardItemModel(4, 4)
        self.model.setHorizontalHeaderLabels(['标题1', '标题2', '标题3', '标题4'])
        for row in range(6):
            for column in range(4):
                item = QStandardItem("row %s, column %s" % (row, column))
                self.model.setItem(row, column, item)
        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        dlgLayout = QVBoxLayout()
        self.btn = QPushButton("删除选中行")
        self.btn.clicked.connect(self.delItem)
        dlgLayout.addWidget(self.tableView)
        dlgLayout.addWidget(self.btn)
        self.setLayout(dlgLayout)

    def delItem(self):
        indexes = self.tableView.selectionModel().selection().indexes()
        if len(indexes) > 0:
            index = indexes[0]
            self.model.removeRows(index.row(), 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = Table()
    table.show()
    sys.exit(app.exec_())
