# -*- coding:utf-8 -*-
# Time : 2019/10/05 上午 9:29 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : CallWeatherWin.py 
# @software: PyCharm


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from 综合应用.getCityWeather.WeatherWin import Ui_Form
import requests


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.cityCode = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def queryWeather(self):
        print("* queryWeather")
        cityName = self.ui.weatherComboBox.currentText()
        self.transCityName(cityName)
        req = requests.get('http://weather.com.cn/data/sk/' + self.cityCode + '.html')
        req.encoding = 'utf-8'
        print(req.json())
        msg1 = '时间：%s' % req.json()['weatherinfo']['time'] + '\n'
        msg2 = '城市：%s' % req.json()['weatherinfo']['city'] + '\n'
        msg3 = '城市代码：%s' % req.json()['weatherinfo']['cityid'] + '\n'
        msg4 = '风向：%s' % req.json()['weatherinfo']['WD'] + '\n'
        msg5 = '温度：%s' % req.json()['weatherinfo']['temp'] + "度\n"
        msg6 = '风力：%s' % req.json()['weatherinfo']['WS'] + '\n'
        msg7 = '湿度：%s' % req.json()['weatherinfo']['SD'] + '\n'
        msg8 = '气压：%s' % req.json()['weatherinfo']['AP']
        result = msg1 + msg2 + msg3 + msg4 + msg5 + msg6 + msg7 + msg8
        self.ui.resultText.setText(result)

    def transCityName(self, cityName):
        if cityName == '陆丰':
            self.cityCode = '101282103'
        elif cityName == '北京':
            self.cityCode = '101010100'
        elif cityName == '天津':
            self.cityCode = '101030100'
        elif cityName == '上海':
            self.cityCode = '101020100'

    def clearResult(self):
        self.ui.resultText.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
