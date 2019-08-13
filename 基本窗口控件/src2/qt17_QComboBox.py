# -*- coding:utf-8 -*-
# Time : 2019/08/13 上午 9:23 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt17_QComboBox.py 
# @software: PyCharm

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ComboBoxDemo(QWidget):
    def __init__(self, parent=None):
        super(ComboBoxDemo, self).__init__(parent)
        self.setWindowTitle("QComboBox 示例")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(300, 90)
        layout = QVBoxLayout()
        self.lbl = QLabel()

        self.cb = QComboBox()
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])
        self.cb.currentIndexChanged.connect(self.selectionChange)
        layout.addWidget(self.cb)
        layout.addWidget(self.lbl)
        self.setLayout(layout)

    def selectionChange(self, i):
        self.lbl.setText(self.cb.currentText())
        print("Item in the list are:")
        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))
            print("Current index", i, "selection changed", self.cb.currentText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    comboBox = ComboBoxDemo()
    comboBox.show()
    sys.exit(app.exec_())
