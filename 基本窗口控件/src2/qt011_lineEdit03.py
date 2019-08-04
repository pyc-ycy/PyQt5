# -*- coding:utf-8 -*-
# Time : 2019/08/04 上午 8:51 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : qt011_lineEdit03.py 
# @software: PyCharm

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
import sys


class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit 掩码示例")

        flo = QFormLayout()
        pIPLineEdit = QLineEdit()
        pMACLineEdit = QLineEdit()
        pDateLineEdit = QLineEdit()
        pLicenseLineEdit = QLineEdit()

        pIPLineEdit.setInputMask("000.000.000.000;_")
        pMACLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        pDateLineEdit.setInputMask("0000-00-00")
        pLicenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        flo.addRow("IP 掩码:", pIPLineEdit)
        flo.addRow("Mac 掩码:", pMACLineEdit)
        flo.addRow("日期掩码:", pDateLineEdit)
        flo.addRow("许可证掩码:", pLicenseLineEdit)

        self.setLayout(flo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())