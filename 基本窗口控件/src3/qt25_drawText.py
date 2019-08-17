# -*- coding:utf-8 -*-
# Time : 2019/08/17 下午 3:50 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt25_drawText.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Drawing(QWidget):
    def __init__(self, parent=None):
        super(Drawing, self).__init__(parent)
        self.setWindowTitle("在窗口中绘制文字")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.resize(300, 200)
        self.text = "欢迎学习 PyQt5"

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        # 自定义绘制方法
        self.draw_text(event, painter)
        painter.end()

    def draw_text(self, event, qp):
        # 设置画笔颜色
        qp.setPen(QColor(168, 34, 3))
        # 设置字体
        qp.setFont(QFont('SimSun', 20))
        # 绘制文字
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Drawing()
    demo.show()
    sys.exit(app.exec_())
