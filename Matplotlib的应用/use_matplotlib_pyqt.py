# -*- coding:utf-8 -*-
# Time : 2019/10/04 下午 5:12 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : use_matplotlib_pyqt.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Matplotlib的应用.matplotlib_pyqt import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Matplotlib Using")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setupUi(self)
        # self.matplotlibwidget_dynamic.setStaticVisible(False)
        # self.matplotlibwidget_static.setDynamicVisible(False)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        # self.matplotlibwidget_static.setStaticVisible(True)
        self.matplotlibwidget_static.mpl.start_static_plot()

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        # self.matplotlibwidget_dynamic.setDynamicVisible(True)
        self.matplotlibwidget_dynamic.mpl.start_dynamic_plot()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
