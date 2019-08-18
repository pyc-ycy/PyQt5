# -*- coding:utf-8 -*-
# Time : 2019/08/18 下午 3:32 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt33_DateTimeEditTest.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DateTimeEditDemo(QWidget):
    def __init__(self):
        super(DateTimeEditDemo, self).__init__()
        self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.btn = QPushButton("获得日期和时间")

        self.initUI()

    def initUI(self):
        self.setWindowTitle("QDateTimeEdit 例子")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(300, 90)

        layout = QVBoxLayout()
        self.dateEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.dateEdit.setMinimumDate(QDate.currentDate().addDays(-365))
        self.dateEdit.setMaximumDate(QDate.currentDate().addDays(365))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.dateChanged.connect(self.onDateChanged)
        self.dateEdit.dateTimeChanged.connect(self.onDateTimeChanged)
        self.dateEdit.timeChanged.connect(self.onTimeChanged)

        self.btn.clicked.connect(self.onButtonClick)

        layout.addWidget(self.dateEdit)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def onDateChanged(self, date):
        print(date)

    def onDateTimeChanged(self, dateTime):
        print(dateTime)

    def onTimeChanged(self, time):
        print(time)

    def onButtonClick(self):
        dateTime = self.dateEdit.dateTime()
        maxDate = self.dateEdit.maximumDate()
        maxDateTime = self.dateEdit.maximumDateTime()
        maxTime = self.dateEdit.maximumTime()
        minDate = self.dateEdit.minimumDate()
        minDateTime = self.dateEdit.minimumDateTime()
        minTime = self.dateEdit.minimumTime()
        print('\n选择日期时间')
        print('dateTime=%s' % str(dateTime))
        print('maxDate=%s' % str(maxDate))
        print('maxDateTime=%s' % str(maxDateTime))
        print('maxTime=%s' % maxTime)
        print('minDate=%s' % str(minDate))
        print('minDateTime=%s' % str(minDateTime))
        print('minTime=%s' % str(minTime))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = DateTimeEditDemo()
    demo.show()
    sys.exit(app.exec_())
