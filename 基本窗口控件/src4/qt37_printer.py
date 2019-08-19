# -*- coding:utf-8 -*-
# Time : 2019/08/19 下午 9:04 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt37_printer.py 
# @software: PyCharm


import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.PrintAction = QAction(QIcon("./images/printer.png"), self.tr("打印"), self)
        self.setWindowTitle(self.tr("打印图片"))
        self.setWindowIcon(QIcon("./images/Python2.ico"))
        self.imageLabel = QLabel()
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setCentralWidget(self.imageLabel)
        self.image = QImage()
        self.createActions()
        self.createMenus()
        self.createToolBars()

        if self.image.load("./images/back.jpg"):
            self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
            self.resize(self.image.width(), self.image.height())

    def createActions(self):
        self.PrintAction.setShortcut("Ctrl+P")
        self.PrintAction.setStatusTip(self.tr("打印"))
        self.PrintAction.triggered.connect(self.slotPrint)

    def createMenus(self):
        PrintMenu = self.menuBar().addMenu(self.tr("打印"))
        PrintMenu.addAction(self.PrintAction)

    def createToolBars(self):
        fileToolBar = self.addToolBar("Print")
        fileToolBar.addAction(self.PrintAction)

    def slotPrint(self):
        printer = QPrinter()
        printDialog = QPrintDialog()
        if printDialog.exec_():
            painter = QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())