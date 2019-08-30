# -*- coding:utf-8 -*-
# Time : 2019/08/30 上午 9:29 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : WebViewJSTest01.py 
# @software: PyCharm


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle('加载 JavaScript 示例')
win.setWindowIcon(QIcon("./images/Python2.ico"))
layout = QVBoxLayout()
win.setLayout(layout)
view = QWebEngineView()
view.setHtml(
    '''
        <html>
            <head>
                <title>A Demo Page</title>
                <script language="javascript">
                    // 获得输入的姓名，然后在页面中显示提交按钮
                    function completeAndReturnName(){
                        var fname = document.getElementById('fname').value;
                        var lname = document.getElementById('lname').value;
                        var full = fname + ' ' + lname;
                
                        document.getElementById('fullname').value = full;
                        document.getElementById('submit-btn').style.display = 'block';
                
                        return full;
                    }
                </script>
            </head>
            <body>
                <form>
                    <label for="fname">First name:</label>
                    <input type="text" name="fname" id="fname"></input>
                    <br />
                    <label for="lname">Last name:</label>
                    <input type="text" name="lname" id="lname"></input>
                    <br />
                    <label for="fullname">Full name:</label>
                    <input disabled type="text" name="fullname" id="fullname"></input>
                    <br />
                    <input style="display: none;" type="submit" id="submit-btn"></input>
                </form>
            </body>
        </html>
    '''
)
# 创建一个调用 JavaScript 代码的按钮
button = QPushButton('设置全名')


def js_callback(result):
    print(result)


def complete_name():
    view.page().runJavaScript('completeAndReturnName();', js_callback)


button.clicked.connect(complete_name)
layout.addWidget(view)
layout.addWidget(button)
win.show()
sys.exit(app.exec_())
