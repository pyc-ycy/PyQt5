# -*- coding:utf-8 -*-
# Time : 2019/08/01 下午 6:38 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt07_QLabel.py 
# @software: PyCharm


from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QIcon
import sys


class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        # 1 初始化标签
        label1.setText("这是一个文本标签。")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用 Python GUI 应用</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./images/python.jpg"))

        label4.setText("<A href='https://blog.csdn.net/qq_42896653/article/category/9162463'>欢迎访问御承扬的PyQt5主题的博客</A>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个超链接标签")

        # 2 在窗口布局中添加控件
        vBox = QVBoxLayout()
        vBox.addWidget(label1)
        vBox.addStretch()
        vBox.addWidget(label2)
        vBox.addStretch()
        vBox.addWidget(label3)
        vBox.addStretch()
        vBox.addWidget(label4)

        # 3 允许 label1 控件访问超链接
        label1.setOpenExternalLinks(True)
        label4.setOpenExternalLinks(False)
        # 点击文本框绑定槽事件
        label4.linkActivated.connect(link_clicked)

        # 滑过文本框绑定槽事件
        label2.linkHovered.connect(link_hovered)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.setLayout(vBox)
        self.setWindowTitle("QLabel 例子")
        self.setWindowIcon(QIcon("Python2.ico"))


def link_hovered():
    print("当鼠标滑过 label2 标签时，触发事件")


def link_clicked():
    print("当鼠标点击 label4 标签时，触发事件")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.show()
    sys.exit(app.exec_())
