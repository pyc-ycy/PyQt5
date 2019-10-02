# -*- coding:utf-8 -*-
# Time : 2019/10/02 下午 3:35 
# Author : 御承扬
# e-mail:2923616405@qq.com
# project:  PyQt5
# File : testing.py 
# @software: PyCharm


from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
import pandas
import numpy
import sys
from qtpandas.excepthook import excepthook

# Use QtGui from the compat module to take care if correct sip version, etc.
from qtpandas.compat import QtGui
from qtpandas.models.DataFrameModel import DataFrameModel
from qtpandas.views.DataTableView import DataTableWidget

# from qtpandas.views._ui import icons_rc


if __name__ == '__main__':
    standard_library.install_aliases()
    sys.excepthook = excepthook
    model = DataFrameModel()
    app = QtGui.QApplication([])
    widget = DataTableWidget()
    widget.resize(500, 300)
    widget.show()
    widget.setViewModel(model)
    data = {
        'A': [10, 11, 12],
        'B': [20, 21, 22],
        'C': ['Peter Pan', 'Cpt. Hook', 'Tinkerbell']
    }
    df = pandas.DataFrame(data)
    df['A'] = df['A'].astype(numpy.int8)
    df['B'] = df['B'].astype(numpy.float16)
    model.setDataFrame(df)
    app.exec_()
