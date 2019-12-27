# PyCharm
# PyQt5
# callTest
# 御承扬
# 2019/12/26


from PyQt5.QtWidgets import QMainWindow, QApplication
from fileofdesinger.test import Ui_MainWindow
import sys


class testUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(testUI, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = testUI()
    ui.show()
    sys.exit(app.exec_())
