# -*- coding:utf-8 -*-
# Time : 2019/08/13 上午 11:10 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt18_QSpinBox.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class spinDemo(QWidget):
    def __init__(self, parent=None):
        super(spinDemo, self).__init__(parent)
        self.setWindowTitle("QSpinBox 示例")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.label = QLabel("current value:")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.sp = QSpinBox()
        layout.addWidget(self.sp)
        self.sp.valueChanged.connect(self.changedValue)
        self.setLayout(layout)

    def changedValue(self):
        self.label.setText("current value:" + str(self.sp.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = spinDemo()
    win.show()
    sys.exit(app.exec_())