# -*- coding:utf-8 -*-
# Time : 2019/09/15 下午 4:38 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : SignalSlot5.py 
# @software: PyCharm


from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinForm(QMainWindow):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setWindowTitle('Signal Demo')
        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')
        button1.clicked.connect(lambda: self.onButtonClick(1))
        button2.clicked.connect(lambda: self.onButtonClick(2))
        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self, n):
        print('Button{0} 被按下了'.format(n))
        QMessageBox.information(self, "信息提示框", 'Button{0} clicked'.format(n))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
