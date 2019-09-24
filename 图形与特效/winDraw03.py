# -*- coding:utf-8 -*-
# Time : 2019/09/24 下午 5:34 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : winDraw03.py 
# @software: PyCharm


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setWindowTitle("使用双缓冲绘图示例")
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        # 辅助画布
        self.tempPix = QPixmap()
        # 标志是否正在绘图
        self.isDrawing = False
        self.initUI()

    def initUI(self):
        self.resize(600, 500)
        self.pix = QPixmap(400, 400)
        self.pix.fill(Qt.white)

    def paintEvent(self, event):
        painter = QPainter(self)
        x = self.lastPoint.x()
        y = self.lastPoint.y()
        w = self.endPoint.x() - x
        h = self.endPoint.y() - y
        if self.isDrawing:
            self.tempPix = self.pix
            pp = QPainter(self.tempPix)
            pp.drawRect(x, y, w, h)
            painter.drawPixmap(0, 0, self.tempPix)
        else:
            pp = QPainter(self.pix)
            pp.drawRect(x, y, w, h)
            painter.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint
            self.isDrawing = True

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()
            self.isDrawing = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
