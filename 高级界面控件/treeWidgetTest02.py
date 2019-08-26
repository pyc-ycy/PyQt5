# -*- coding:utf-8 -*-
# Time : 2019/08/26 下午 2:26 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : treeWidgetTest02.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TreeWidgetDemo(QMainWindow):
    def __init__(self, parent=None):
        super(TreeWidgetDemo, self).__init__(parent)
        self.setWindowTitle("TreeWidget 例子")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(340, 250)
        self.tree = QTreeWidget()
        # 设置列数
        self.tree.setColumnCount(2)
        # 设置头的标题
        self.tree.setHeaderLabels(['Key', 'Value'])
        # 设置根节点
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        root.setText(1, '0')

        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, '1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '2')

        child3 = QTreeWidgetItem(root)
        child3.setText(0, 'child3')
        child3.setText(1, '3')

        child4 = QTreeWidgetItem(child3)
        child4.setText(0, 'child4')
        child4.setText(1, '4')

        child5 = QTreeWidgetItem(child3)
        child5.setText(0, 'child5')
        child5.setText(1, '5')

        self.tree.addTopLevelItem(root)
        self.tree.clicked.connect(self.onTreeClicked)
        self.setCentralWidget(self.tree)

    def onTreeClicked(self, qModelIndex):
        item = self.tree.currentItem()
        print("Key=%s, Value=%s" % (item.text(0), item.text(1)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TreeWidgetDemo()
    win.show()
    sys.exit(app.exec_())