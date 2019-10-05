# -*- coding:utf-8 -*-
# Time : 2019/10/05 上午 8:40 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : getWeatherInfo.py 
# @software: PyCharm


import requests

if __name__ == "__main__":
    req = requests.get('http://www.weather.com.cn/data/sk/101282103.html')
    req.encoding = 'utf-8'
    print('返回结果：%s' % req.json())
    print('时间：%s' % req.json()['weatherinfo']['time'])
    print('城市：%s' % req.json()['weatherinfo']['city'])
    print('城市代码：%s' % req.json()['weatherinfo']['cityid'])
    print('风向：%s' % req.json()['weatherinfo']['WD'])
    print('温度：%s' % req.json()['weatherinfo']['temp'] + "度")
    print('风力：%s' % req.json()['weatherinfo']['WS'])
    print('湿度：%s' % req.json()['weatherinfo']['SD'])
    print('气压：%s' % req.json()['weatherinfo']['AP'])
