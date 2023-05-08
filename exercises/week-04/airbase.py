# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:35:40 2015

@author: joris
"""

import os
import pandas as pd


def read_file(filename):
    _, fname = os.path.split(filename)
    station = fname[:7]

    # colnames = ['date'] + [item for pair in zip(["{:02d}".format(i) for i in range(24)], ['flag']*24) for item in pair]
    # data = pd.read_csv(filename, sep='\t', header=None,
    #                    na_values=[-999, -9999], names=colnames, index_col='date')

    data = pd.read_csv(filename, sep='\t', header=None, 
			na_values=[-999, -9999], index_col=0)

    # drop the flags
    data = data.drop(data.columns[1::2], axis=1)

    data.columns = ["{:02d}".format(i) for i in range(len(data.columns))]

    data = data.stack()
    data = data.reset_index(name=station)
    data = data.rename(columns = {0:'date', 'level_1':'hour'})
    data.index = pd.to_datetime(data['date'] + ' ' + data['hour'])
    data = data.drop(['date', 'hour'], axis=1)
    # data.head()

    return data


def load_data():


    #os.chdir("/data/Scipy/PyData Paris 2015/2015-PyData-Paris-pandas-intro")

    files = ["data/input/BETR8010000800100hour.1-1-1990.31-12-2012",
             "data/input/BETN0290000800100hour.1-1-1990.31-12-2012",
             "data/input/FR040370000800100hour.1-1-1999.31-12-2012",
             "data/input/FR040120000800100hour.1-1-1999.31-12-2012"]

    data = []

    for fname in files:
        df = read_file(fname)
        data.append(df)

    data = pd.concat(data, axis=1)

    return data
