# -*- coding:utf-8 -*-
# Time : 2019/08/17 下午 12:43 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt24_FileDialog.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class fileDialogDemo(QWidget):
    def __init__(self, parent=None):
        super(fileDialogDemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.btn = QPushButton("加载图片")
        self.btn.clicked.connect(self.GetFile)
        self.le = QLabel("")
        layout.addWidget(self.btn)
        layout.addWidget(self.le)
        self.btn1 = QPushButton("加载文本文件")
        self.btn1.clicked.connect(self.GetFiles)
        layout.addWidget(self.btn1)
        self.contents = QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("FileDialog 例子")
        self.setWindowIcon(QIcon("./images/Python2.ico"))

    def GetFile(self):
        f_name, _ = QFileDialog.getOpenFileName(self, 'Open File', 'D:\\', "Image files(*.jpg *.gif)")
        self.le.setPixmap(QPixmap(f_name))

    def GetFiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)

        if dlg.exec_():
            filename = dlg.selectedFiles()
            f = open(filename[0], 'r')

            with f:
                data = f.read()
                self.contents.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = fileDialogDemo()
    win.show()
    sys.exit(app.exec_())
