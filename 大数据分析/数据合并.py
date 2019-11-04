# -*- coding:utf-8 -*-
# Time : 2019/10/22 下午 8:32 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : 数据合并.py 
# @software: PyCharm


import pandas as pd
from pandas import read_excel

if __name__ == "__main__":
    # 示例1 记录合并
    # df1 = read_excel(r'.\data\i_nuc.xls', sheet_name='Sheet3')
    # print(df1.head())
    # df2 = read_excel(r'.\data\i_nuc.xls', sheet_name='Sheet5')
    # print(df2)
    # df = pd.concat([df1, df2], ignore_index=True)
    # print(df)
    # df = pd.DataFrame(
    #     {'band': [189, 135, 134, 133],
    #      'area': ['0351', '0352', '0354', '0341'],
    #      'num': [2190, 8513, 8080, 7890]}
    # )
    # print(df)
    # df = df.astype(str)
    # tel = df['band'] + df['area'] + df['num']
    # print(tel)
    # df['tel'] = tel
    # print(df)
    # df1 = read_excel(r'.\data\i_nuc.xls', sheet_name='Sheet3')
    # df2 = read_excel(r'.\data\i_nuc.xls', sheet_name='Sheet4')
    # print(df1.head())
    # print(df2.head())
    # df = pd.merge(df1, df2, left_on='学号', right_on='学号')
    # print(df.head())
    df1 = pd.DataFrame(
        {'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
         'data1': range(7)}
    )
    print(df1)
    df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})
    print(df2)
    print(df1.merge(df2, on='key', how='right'))
    print(df1.merge(df2, on='key', how='outer'))
