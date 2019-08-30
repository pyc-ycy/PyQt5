# -*- coding:utf-8 -*-
# Time : 2019/08/30 下午 9:21 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : MyShareObject.py 
# @software: PyCharm


from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import QWidget, QMessageBox


class MyShareObject(QWidget):
    def __init__(self):
        super(MyShareObject, self).__init__()

    def _getStrValue(self):
        return '100'

    def _setStrValue(self, str):
        print('获得页面参数：%s' % str)
        QMessageBox.information(self, "Information", '获得页面参数：%s' % str)

    strValue = pyqtProperty(str, fget=_getStrValue, fset=_setStrValue)
