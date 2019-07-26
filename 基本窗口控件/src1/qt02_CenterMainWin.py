# -*- coding:utf-8 -*-
# Time : 2019/07/26 下午 6:35 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt02_CenterMainWin.py 
# @software: PyCharm


from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow
import sys


class WinForm(QMainWindow):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)

        self.setWindowTitle("主窗口放置在屏幕中间的例子")
        self.resize(370, 250)
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        x: int = int((screen.width() - size.width()) / 2)
        y: int = int((screen.height() - size.height()) / 2)
        self.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
