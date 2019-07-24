# -*- coding:utf-8 -*-
# Time : 2019/07/23 下午 7:54 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : call_layoutTest.py 
# @software: PyCharm

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from 初识PyQt5.layoutTest import Ui_LayoutDemo


class LayoutDemo(QMainWindow, Ui_LayoutDemo):
    """
    CLass documentation goes here
    """

    def __init__(self, parent=None):
        """
        Constructor


        @:param parent reference to the parent widget
        @:type QWidget
        """
        super(LayoutDemo, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here
        :return:
        """
        print('收益_min:', self.doubleSpinBox_returns_min.text())
        print('收益_max:', self.doubleSpinBox_returns_max.text())
        print('最大回撤_min:', self.doubleSpinBox_maxdrawdown_min.text())
        print('最大回撤_max:', self.doubleSpinBox_maxdrawdown_max.text())
        print('sharp 比_min:', self.doubleSpinBox_sharp_min.text())
        print('sharp 比_max:', self.doubleSpinBox_sharp_max.text())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = LayoutDemo()
    ui.show()
    sys.exit(app.exec_())
