# -*- coding: utf-8 -*-
# @Time:2018/08/29
# @Author :tang
from pandas import read_csv
from matplotlib import pyplot as plt
def load(csvfile):
    data = read_csv(csvfile,index_col=0)
    X = data.values[:,0]
    y = data.values[:,1]
    plt.scatter(X,y,marker='x')
    plt.xlabel('population of city in 10,000s')
    plt.ylabel('profit in $10,000s')
    plt.show()
    return X,y

# load(csvfile='ex1data1.csv')
def computeCost():
    """

    :return:
    """