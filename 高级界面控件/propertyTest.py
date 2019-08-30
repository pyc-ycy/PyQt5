# -*- coding:utf-8 -*-
# Time : 2019/08/30 下午 5:28 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : propertyTest.py 
# @software: PyCharm


from PyQt5.QtCore import pyqtProperty, QObject


class MyObject(QObject):
    def __init__(self, inVal=20):
        super().__init__()
        self.val = inVal

    def readVal(self):
        print("readVal=%s" % self.val)
        return self.val

    def setVal(self, val):
        print("setVal=%s" % val)
        self.val = val

    ppVal = pyqtProperty(int, readVal, setVal)


if __name__ == "__main__":
    obj = MyObject()
    print('\n#1')
    obj.ppVal = 10
    print('\n#2')
    print('obj.ppVal=%s' % obj.ppVal)
    print('obj.readVal()=%s' % obj.readVal())
