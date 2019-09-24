# -*- coding:utf-8 -*-
# Time : 2019/09/23 下午 4:09 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : winDraw01.py 
# @software: PyCharm


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setWindowTitle("绘图示例")
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endpoint = QPoint()
        self.initUI()

    def initUI(self):
        self.resize(600, 500)
        self.pix = QPixmap(400, 400)
        self.pix.fill(Qt.white)

    def paintEvent(self, event):
        pp = QPainter(self.pix)
        pp.drawLine(self.lastPoint, self.endpoint)
        self.lastPoint = self.endpoint
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endpoint = self.lastPoint

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.endpoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endpoint = event.pos()
            self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
