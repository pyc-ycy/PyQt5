# PyCharm
# PyQt5
# dbTest
# 御承扬
# 2019/12/2

from PyQt5.QtWidgets import *
import sys
import pymysql


class DBTest(QWidget):
    def __init__(self):
        super(DBTest, self).__init__(parent=None)
        self.setWindowTitle("连接数据库查询")
        self.resize(300, 270)
        self.textEdit = QTextEdit()
        self.btn = QPushButton("连接并查询")
        self.lbl = QLabel("username：")
        self.lineEdit = QLineEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.lbl)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.btn)
        self.setLayout(layout)
        self.btn.clicked.connect(self.conn)

    def conn(self):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root19537',
            db='test',
            charset='utf8'
        )
        if conn:
            print('成功连接数据库！！！')
            s = str.format("select * from tb_user where username like '{}%'", self.lineEdit.text())
            cursor = conn.cursor()
            cursor.execute(s)
            result = cursor.fetchall()
            self.textEdit.setPlainText("username\tpassword\tsex\t\n")
            for row in result:
                self.textEdit.setPlainText(row[0] + " " + row[1] + " " + row[2])

            conn.close()
        else:
            self.textEdit.setText("数据库连接失败")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DBTest()
    win.show()
    sys.exit(app.exec_())
