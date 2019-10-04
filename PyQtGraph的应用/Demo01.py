# -*- coding:utf-8 -*-
# Time : 2019/10/04 下午 7:51 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : Demo01.py 
# @software: PyCharm


import pyqtgraph as pg
import numpy as np

if __name__ == "__main__":
    win = pg.GraphicsWindow(title="Basic plotting examples")
    pl = win.addPlot(title="Basic array plotting", y=np.random.normal(size=100))
