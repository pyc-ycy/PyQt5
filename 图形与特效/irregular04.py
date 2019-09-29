# -*- coding:utf-8 -*-
# Time : 2019/09/29 下午 7:39 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : irregular04.py 
# @software: PyCharm


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.i = 1
        self.pic = None
        self.pix = None
        self.dragPosition = None
        self.m_drag = None
        self.m_DragPosition = None
        self.drawPix()
        self.timer = QTimer()
        self.timer.setInterval(500)  # 定时器每 500 毫秒更新一次
        self.timer.timeout.connect(self.timeChange)
        self.timer.start()

    def drawPix(self):
        self.update()
        if self.i == 5:
            self.i = 1
        self.pic = {1: './images/left.png', 2: './images/up.png',
                    3: './images/right.png', 4: './images/down.png'}
        self.pix = QPixmap(self.pic[self.i], '0', Qt.AvoidDither | Qt.ThresholdDither | Qt.ThresholdAlphaDither)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.dragPosition = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
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
        if event.button() == 1:
            self.i += 1
            self.drawPix()

    def timeChange(self):
        self.i += 1
        self.drawPix()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
