# -*- coding:utf-8 -*-
# Time : 2019/09/28 上午 9:44 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : example_pyqt5.py 
# @software: PyCharm


import qdarkstyle
from PyQt5.QtGui import QIcon

from 图形与特效.ui import example_pyqt5_ui as example_ui
import logging
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from os.path import abspath, dirname

sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))


def main():
    logging.basicConfig(level=logging.DEBUG)
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    ui = example_ui.Ui_MainWindow()
    ui.setupUi(window)
    ui.bt_delay_popup.addActions([
        ui.actionAction,
        ui.actionAction_C
    ])
    ui.bt_menu_button_popup.addActions([
        ui.actionAction,
        ui.actionAction_C
    ])
    item = QtWidgets.QTableWidgetItem("Test")
    item.setCheckState(QtCore.Qt.Checked)
    ui.tableWidget.setItem(0, 0, item)
    window.setWindowTitle("QDarkStyle example")
    window.setWindowIcon(QIcon("./images/Python2.ico"))
    window.tabifyDockWidget(ui.dockWidget1, ui.dockWidget2)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    if "--travis" in sys.argv:
        QtCore.QTimer.singleShot(2000, app.exit)
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
