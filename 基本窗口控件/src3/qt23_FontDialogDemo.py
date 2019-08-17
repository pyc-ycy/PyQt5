# -*- coding:utf-8 -*-
# Time : 2019/08/17 上午 10:38 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt23_FontDialogDemo.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class FontDialogDemo(QWidget):
    def __init__(self, parent=None):
        super(FontDialogDemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.fontButton = QPushButton("选择字体")
        self.fontButton.clicked.connect(self.GetFont)
        layout.addWidget(self.fontButton)
        self.label = QLabel("Hello，测试字体例子")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setWindowTitle("FontDialog 例子")
        self.setWindowIcon(QIcon("./images/Python2.ico"))

    def GetFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = FontDialogDemo()
    win.show()
    sys.exit(app.exec_())