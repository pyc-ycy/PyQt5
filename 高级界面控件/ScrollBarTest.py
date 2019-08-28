# -*- coding:utf-8 -*-
# Time : 2019/08/28 上午 9:06 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : ScrollBarTest.py
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.l1 = QLabel("拖动滑块改变颜色")
        self.s1 = QScrollBar()
        self.s2 = QScrollBar()
        self.s3 = QScrollBar()
        self.initUI()

    def initUI(self):
        hBox = QHBoxLayout()
        self.l1.setFont(QFont("Arial", 16))
        hBox.addWidget(self.l1)
        self.s1.setMaximum(255)
        self.s1.sliderMoved.connect(self.sliderVal)
        self.s2.setMaximum(255)
        self.s2.sliderMoved.connect(self.sliderVal)
        self.s3.setMaximum(255)
        self.s3.sliderMoved.connect(self.sliderVal)
        hBox.addWidget(self.s1)
        hBox.addWidget(self.s2)
        hBox.addWidget(self.s3)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QScrollBar 例子')
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setLayout(hBox)

    def sliderVal(self):
        print(self.s1.value(), self.s2.value(), self.s3.value())
        palette = QPalette()
        c = QColor(self.s1.value(), self.s2.value(), self.s3.value(), 255)
        palette.setColor(QPalette.Foreground, c)
        self.l1.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Example()
    demo.show()
    sys.exit(app.exec_())