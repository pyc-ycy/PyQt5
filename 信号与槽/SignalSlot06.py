# -*- coding:utf-8 -*-
# Time : 2019/09/15 下午 8:13 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : SignalSlot06.py 
# @software: PyCharm

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super(CustomWidget, self).__init__(parent)
        self.setWindowTitle('SignalSlot Demo')
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.okButton = QPushButton("ok", self)
        self.okButton.setObjectName("okButton")
        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        self.setLayout(layout)
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        QMessageBox.information(self, "信息提示框", "单击了ok按钮")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CustomWidget()
    win.show()
    sys.exit(app.exec_())
