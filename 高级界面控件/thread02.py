# -*- coding:utf-8 -*-
# Time : 2019/08/29 上午 8:54 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : thread02.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

global sec
sec = 0


class WorkedThread(QThread):
    trigger = pyqtSignal(int)

    def __init__(self):
        super(WorkedThread, self).__init__()

    def run(self):
        num = 0
        for i in range(20):
            num += 1
            countTime()
        self.trigger.emit(num)


def countTime():
    global sec
    sec += 1
    lcdNumber.display(sec)


def work():
    timer.start(1000)
    workThread.shart()
    workThread.trigger.connect(timeStop)


def timeStop():
    timer.stop()
    print("运行结束用时", lcdNumber.value())
    global sec
    sec = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    top = QWidget()
    top.setWindowTitle("Thread Test")
    top.setWindowIcon(QIcon('./images/Python2.ico'))
    top.resize(300, 120)

    layout = QVBoxLayout()
    lcdNumber = QLCDNumber()
    layout.addWidget(lcdNumber)
    button = QPushButton("测试")
    layout.addWidget(button)
    timer = QTimer()
    workThread = WorkedThread()
    button.clicked.connect(work)
    timer.timeout.connect(timeStop)
    top.setLayout(layout)
    top.show()
    sys.exit(app.exec_())
