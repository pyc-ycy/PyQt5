# -*- coding:utf-8 -*-
# Time : 2019/10/19 下午 7:22 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : line_point.py 
# @software: PyCharm


import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)
    y1 = np.cos(2 * np.pi * x1) * np.exp(-1 * x1)
    y2 = np.cos(2 * np.pi * x2)
    plt.subplot(2, 1, 1)
    plt.plot(x1, y1, 'yo-')
    plt.title('A tale of 2 subplots')
    plt.ylabel('Damped oscillation')
    plt.subplot(2, 1, 2)
    plt.plot(x2, y2, 'r.-')
    plt.xlabel('time(s)')
    plt.ylabel('Undamped')
    plt.show()
