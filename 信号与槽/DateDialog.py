# -*- coding:utf-8 -*-
# Time : 2019/09/16 下午 8:50 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : DateDialog.py 
# @software: PyCharm


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DateDialog(QDialog):
    def __init__(self, parent=None):
        super(DateDialog, self).__init__(parent)
        self.setWindowTitle('DateDialog')
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(100, 100)

        layout = QVBoxLayout(self)
        self.datetime = QDateTimeEdit(self)
        self.datetime.resize(150, 20)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())

        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def dateTime(self):
        return self.datetime.dateTime()

    @staticmethod
    def getDateTime(parent=None):
        dialog = DateDialog(parent)
        result = dialog.exec_()
        date = dialog.dateTime()
        return (date.date(), date.time(), result == QDialog.Accepted)
