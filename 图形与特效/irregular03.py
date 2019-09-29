# -*- coding:utf-8 -*-
# Time : 2019/09/29 上午 11:11 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : irregular03.py 
# @software: PyCharm


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.m_drag = None
        self.m_DragPosition = None
        self.dragPosition = None
        self.pic = None
        self.pix = None
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setWindowTitle("Irregular Window Can Drag")
        self.drawPix()

    def drawPix(self):
        # self.pic = './images/雅男.jpg'
        self.pic = "./images/抠图-1.png"
        self.pix = QPixmap(self.pic, "0", Qt.AvoidDither | Qt.ThresholdDither | Qt.ThresholdAlphaDither)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.dragPosition = None

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def mouseDoubleClickEvent(self, event):
        self.drawPix()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
