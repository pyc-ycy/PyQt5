# -*- coding:utf-8 -*-
# Time : 2019/09/15 下午 4:00 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : SignalSlot04.py 
# @software: PyCharm


from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class CustomSignal(QObject):
    # 声明无参信号
    signal1 = pyqtSignal()
    # 声明带一个 int 型参数的信号
    signal2 = pyqtSignal(int)
    # 声明一个带 int 型和 str 型的参数的信号
    signal3 = pyqtSignal(int, str)
    # 声明一个带列表类型的参数的信号
    signal4 = pyqtSignal(list)
    # 声明一个带字典类型参数的信号
    signal5 = pyqtSignal(dict)
    # 声明一个多重载版本的信号
    signal6 = pyqtSignal([int, str], [str])

    def __init__(self, parent=None):
        super(CustomSignal, self).__init__(parent)
        # 将信号连接到指定槽函数
        self.signal1.connect(self.signalCall1)
        self.signal2.connect(self.signalCall2)
        self.signal3.connect(self.signalCall3)
        self.signal4.connect(self.signalCall4)
        self.signal5.connect(self.signalCall5)
        self.signal6[int, str].connect(self.signalCall6)
        self.signal6[str].connect(self.signalCall6OverLoad)

        # 发射信号
        self.signal1.emit()
        self.signal2.emit(2)
        self.signal3.emit(1, "text")
        self.signal4.emit([1, 2, 3, 4])
        self.signal5.emit({"name": "solder", "age": "24"})
        self.signal6[int, str].emit(1, "text")
        self.signal6[str].emit("text")

    def signalCall1(self):
        print("signal1 emit")

    def signalCall2(self, val):
        print("signal2 emit, value:", val)

    def signalCall3(self, val, text):
        print("signal3 emit, value:", val, text)

    def signalCall4(self, val):
        print("signal4 emit, value:", val)

    def signalCall5(self, val):
        print("signal5 emit, value:", val)

    def signalCall6(self, val, text):
        print("signal6 emit, value:", val, text)

    def signalCall6OverLoad(self, val):
        print("signal6 overload emit, value:", val)


if __name__ == "__main__":
    test = CustomSignal()
