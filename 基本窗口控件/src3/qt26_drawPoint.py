# -*- coding:utf-8 -*-
# Time : 2019/08/17 下午 4:56 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt26_drawPoint.py 
# @software: PyCharm


import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Drawing(QWidget):
    def __init__(self, parent=None):
        super(Drawing, self).__init__(parent)
        self.resize(300, 200)
        self.setWindowTitle("在窗口中画点")
        self.setWindowIcon(QIcon("./images/Python2.ico"))

    def paintEvent(self, event):
        # 初始化绘图工具
        qp = QPainter()
        qp.begin(self)
        # 自定义画点方法
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            # 绘制正弦图形，周期 [-1000,1000]
            x = 100 * (- 1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0
            qp.drawPoint(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Drawing()
    win.show()
    sys.exit(app.exec_())