# -*- coding:utf-8 -*-
# Time : 2019/09/10 下午 8:56 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : pyqtSignalTest.py 
# @software: PyCharm


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


# 信号对象
class QTypeSignal(QObject):
    sendMsg = pyqtSignal(object)

    def __init__(self):
        super(QTypeSignal, self).__init__()

    def run(self):
        self.sendMsg.emit('Hello PyQt5')


# 槽对象
class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot, self).__init__()

    def get(self, msg):
        print("QSlot get msg =>" + msg)


if __name__ == "__main__":
    send = QTypeSignal()
    slot = QTypeSlot()
    print('-----把信号绑定到槽函数上------')
    send.sendMsg.connect(slot.get)
    send.run()
    print('-----把信号与槽函数的连接断开----')
    send.sendMsg.disconnect(slot.get)
    send.run()
