# -*- coding:utf-8 -*-
# Time : 2019/08/28 上午 10:13 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : timer01.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle("QTimer Demo")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(330, 150)
        self.label = QLabel('显示当前时间')
        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')
        layout = QGridLayout()

        # 初始化一个定时器
        self.timer = QTimer(self)
        # showTime() 方法
        self.timer.timeout.connect(self.showTime)

        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.startBtn, 1, 0)
        layout.addWidget(self.endBtn, 1, 1)
        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)
        self.setLayout(layout)

    def showTime(self):
        # 获取系统现在的时间
        time = QDateTime.currentDateTime()
        # 设置系统时间显示格式
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        # 在标签上显示时间
        self.label.setText(timeDisplay)

    def startTimer(self):
        # 设置时间间隔并启动定时器
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())