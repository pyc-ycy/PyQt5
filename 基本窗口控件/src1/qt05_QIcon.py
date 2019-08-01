# -*- coding:utf-8 -*-
# Time : 2019/08/01 下午 3:28 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt05_QIcon.py 
# @software: PyCharm

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication


# 1 创建一个名为 Icon 的类，继承自 QWidget 类
class Icon(QWidget):
    def __init__(self, parent=None):
        super(Icon, self).__init__(parent)
        self.initUI()

    # 2 初始化窗口
    def initUI(self):
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle("程序图标")
        self.setWindowIcon(QIcon("Python2.ico"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    icon = Icon()
    icon.show()
    sys.exit(app.exec_())
