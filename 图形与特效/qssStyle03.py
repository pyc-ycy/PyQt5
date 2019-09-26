# -*- coding:utf-8 -*-
# Time : 2019/09/26 下午 5:42 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qssStyle03.py 
# @software: PyCharm


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setWindowTitle("QSS Demo")
        self.setGeometry(250, 200, 320, 150)
        combo = QComboBox(self)
        combo.setObjectName('myQComboBox')
        combo.addItem('window')
        combo.addItem('Ubuntu')
        combo.addItem('Red hat')
        combo.move(50, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    qssStyle = '''
        QComboBox#myQComboBox::drop-down {
            image:url(  ./images/dropdown.pn)
        }
    '''
    win.setStyleSheet(qssStyle)
    win.show()
    sys.exit(app.exec_())
