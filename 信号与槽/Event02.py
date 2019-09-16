# -*- coding:utf-8 -*-
# Time : 2019/09/16 下午 7:16 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : Event02.py 
# @software: PyCharm


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class EventFilter(QDialog):
    def __init__(self, parent=None):
        super(EventFilter, self).__init__(parent)
        self.setWindowTitle("事件过滤器")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.label1 = QLabel("请点击")
        self.label2 = QLabel("请点击")
        self.label3 = QLabel("请点击")
        self.LabelState = QLabel("test")
        self.image1 = QImage("images/cartoon1.ico")
        self.image2 = QImage("images/cartoon2.ico")
        self.image3 = QImage("images/cartoon3.ico")
        self.width = 600
        self.height = 300
        self.resize(self.width, self.height)
        self.label1.installEventFilter(self)
        self.label2.installEventFilter(self)
        self.label3.installEventFilter(self)
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(self.label1, 500, 0)
        mainLayout.addWidget(self.label2, 500, 1)
        mainLayout.addWidget(self.label3, 500, 2)
        mainLayout.addWidget(self.LabelState, 600, 1)
        self.setLayout(mainLayout)

    def eventFilter(self, watched, event):
        # 只对 label1 的点击事件进行过滤，重写其行为，其他事件忽略
        if watched == self.label1:
            if event.type() == QEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.LabelState.setText("按下鼠标左键")
                elif mouseEvent.button() == Qt.MidButton:
                    self.LabelState.setText("按下鼠标中键")
                elif mouseEvent.buttons() == Qt.RightButton:
                    self.LabelState.setText("按下了鼠标右键")

                '''装换图片大小'''
                transform = QTransform()
                transform.scale(0.5, 0.5)
                tmp = self.image1.transformed(transform)
                self.label1.setPixmap(QPixmap.fromImage(tmp))
            if event.type() == QEvent.MouseButtonRelease:
                self.LabelState.setText("释放鼠标键")
                self.label1.setPixmap(QPixmap.fromImage(self.image2))
        elif watched == self.label3:
            if event.type() == QEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.LabelState.setText("按下鼠标左键")
                elif mouseEvent.button() == Qt.MidButton:
                    self.LabelState.setText("按下鼠标中键")
                elif mouseEvent.buttons() == Qt.RightButton:
                    self.LabelState.setText("按下了鼠标右键")

                '''装换图片大小'''
                transform = QTransform()
                transform.scale(0.5, 0.5)
                tmp = self.image2.transformed(transform)
                self.label3.setPixmap(QPixmap.fromImage(tmp))
            if event.type() == QEvent.MouseButtonRelease:
                self.LabelState.setText("释放鼠标键")
                self.label3.setPixmap(QPixmap.fromImage(self.image3))
        return QDialog.eventFilter(self, watched, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = EventFilter()
    dialog.show()
    sys.exit(app.exec_())
