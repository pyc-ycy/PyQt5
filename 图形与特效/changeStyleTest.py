# -*- coding:utf-8 -*-
# Time : 2019/09/21 下午 4:02 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : changeStyleTest.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *


class AppWidget(QWidget):
    def __init__(self, parent=None):
        super(AppWidget, self).__init__(parent)
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setWindowTitle('界面风格示例')
        horizontalLayout = QHBoxLayout()
        self.styleLabel = QLabel("Set Style:")
        self.styleComBox = QComboBox()
        self.styleComBox.addItems(QStyleFactory.keys())
        index = self.styleComBox.findText(
            QApplication.style().objectName(),
            QtCore.Qt.MatchFixedString
        )
        self.styleComBox.setCurrentIndex(index)
        self.styleComBox.activated[str].connect(self.handleStyleChanged)
        horizontalLayout.addWidget(self.styleLabel)
        horizontalLayout.addWidget(self.styleComBox)
        self.setLayout(horizontalLayout)

    def handleStyleChanged(self, style):
        QApplication.setStyle(style)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AppWidget()
    win.show()
    sys.exit(app.exec_())
