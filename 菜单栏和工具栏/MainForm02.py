# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm02.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWin02(object):
    def setupUi(self, MainWin02):
        MainWin02.setObjectName("MainWin02")
        MainWin02.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWin02)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 721, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MaingridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MaingridLayout.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout.setObjectName("MaingridLayout")
        MainWin02.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWin02)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        MainWin02.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWin02)
        self.statusbar.setObjectName("statusbar")
        MainWin02.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWin02)
        self.toolBar.setObjectName("toolBar")
        MainWin02.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.fileOpenAction = QtWidgets.QAction(MainWin02)
        self.fileOpenAction.setObjectName("fileOpenAction")
        self.fileNewAction = QtWidgets.QAction(MainWin02)
        self.fileNewAction.setObjectName("fileNewAction")
        self.fileCloseAction = QtWidgets.QAction(MainWin02)
        self.fileCloseAction.setObjectName("fileCloseAction")
        self.addWinAction = QtWidgets.QAction(MainWin02)
        self.addWinAction.setObjectName("addWinAction")
        self.menu_F.addAction(self.fileOpenAction)
        self.menu_F.addAction(self.fileNewAction)
        self.menu_F.addAction(self.fileCloseAction)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.addWinAction)

        self.retranslateUi(MainWin02)
        QtCore.QMetaObject.connectSlotsByName(MainWin02)

    def retranslateUi(self, MainWin02):
        _translate = QtCore.QCoreApplication.translate
        MainWin02.setWindowTitle(_translate("MainWin02", "MainWindow"))
        self.menu_F.setTitle(_translate("MainWin02", "文件(&F)"))
        self.menu_E.setTitle(_translate("MainWin02", "编辑(&E)"))
        self.toolBar.setWindowTitle(_translate("MainWin02", "toolBar"))
        self.fileOpenAction.setText(_translate("MainWin02", "打开"))
        self.fileOpenAction.setShortcut(_translate("MainWin02", "Alt+O"))
        self.fileNewAction.setText(_translate("MainWin02", "新建"))
        self.fileNewAction.setToolTip(_translate("MainWin02", "新建"))
        self.fileNewAction.setShortcut(_translate("MainWin02", "Alt+N"))
        self.fileCloseAction.setText(_translate("MainWin02", "关闭"))
        self.fileCloseAction.setToolTip(_translate("MainWin02", "关闭"))
        self.fileCloseAction.setShortcut(_translate("MainWin02", "Alt+C"))
        self.addWinAction.setText(_translate("MainWin02", "添加窗体"))
        self.addWinAction.setToolTip(_translate("MainWin02", "添加窗体"))

