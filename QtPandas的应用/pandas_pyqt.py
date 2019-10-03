# -*- coding:utf-8 -*-
# Time : 2019/10/03 下午 2:42 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : pandas_pyqt.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from QtPandas的应用.pandastablewidget import Ui_MainWindow
from qtpandas.models.DataFrameModel import DataFrameModel
import pandas as pd


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("QtPandas")
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.setupUi(self)
        widget = self.pandastablewidget
        widget.resize(600, 500)
        self.model = DataFrameModel()
        widget.setViewModel(self.model)
        self.df = pd.read_excel(r'./data/fund_data.xlsx', encoding='gbk')
        self.df_original = self.df.copy()
        self.model.setDataFrame(self.df)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.model.setDataFrame(self.df_original)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.df.to_excel(r'./data/fund_data_new1.xlsx')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
