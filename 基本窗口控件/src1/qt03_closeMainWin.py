# -*- coding:utf-8 -*-
# Time : 2019/07/26 下午 7:22 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt03_closeMainWin.py 
# @software: PyCharm


from PyQt5.QtWidgets import QMainWindow, QHBoxLayout,QPushButton, QApplication, QWidget
import sys


class WinForm(QMainWindow):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('关闭主窗口例子')
        self.button1 = QPushButton('关闭窗口')
        self.button1.clicked.connect(self.onButtonClick)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

        # sender 是发送信号的对象
    def onButtonClick(self):
        sender = self.sender()
        print(sender.text()+'被按下了')
        app = QApplication.instance()
        app.quit()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(App.exec_())