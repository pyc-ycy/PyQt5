# -*- coding:utf-8 -*-
# Time : 2019/10/23 下午 4:33 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : 数据计算.py 
# @software: PyCharm


from pandas import read_excel
import unittest


# 简单计算
def test1():
    df = read_excel("./data/i_nuc.xls", sheet_name="Sheet3")
    print(df.head(10))
    jj = df['解几'].astype(int)
    gd = df['高代'].astype(int)
    df['高代+解几'] = jj + gd
    print(df.head(10))


# min-max 标准化
def test2():
    df = read_excel("./data/i_nuc.xls", sheet_name="Sheet3")
    print(df.head(10))
    scale = (df.数分.astype(int) - df.数分.astype(int).min()) / (
            df.数分.astype(int).max() - df.数分.astype(int).min()
    )
    print(scale.head(10))


def test3(a: int, b: int) -> int:
    return a + b


class Test(unittest.TestCase):
    def test_lcs(self):
        result = test3(2, 5)
        self.assertEqual(result, 7)


if __name__ == "__main__":
    test2()
