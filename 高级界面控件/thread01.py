# -*- coding:utf-8 -*-
# Time : 2019/08/29 上午 8:02 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : thread01.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Worked(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Worked, self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        while self.working:
            file_str = 'File index{0}'.format(self.num)
            self.num += 1
            # 发射信号
            self.sinOut.emit(file_str)
            # 线程休眠两秒
            self.sleep(2)


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setWindowTitle("QThread Demo")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.thread = Worked()
        self.listFile = QListWidget()
        self.btnStart = QPushButton('开始')
        layout = QGridLayout()
        layout.addWidget(self.listFile, 0, 0, 1, 2)
        layout.addWidget(self.btnStart, 1, 1)
        self.btnStart.clicked.connect(self.slotStart)
        self.thread.sinOut.connect(self.slotAdd)
        self.setLayout(layout)
        self.resize(350, 300)

    def slotAdd(self, file_inf):
        self.listFile.addItem(file_inf)

    def slotStart(self):
        self.btnStart.setEnabled(False)
        self.thread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWidget()
    win.show()
    sys.exit(app.exec_())
