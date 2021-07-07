# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Shishao_Zhao"


'''
将从爬虫获取到的数据进行初步处理，
并存入csv文件
'''

from pandas import DataFrame
import pandas as pd
import numpy as np

# 读测试数据
def load_test_data():
    row_stock_data, row_stock_day_data = [], []
    stock_file, stock_day_file = './stock.txt', './stock_day.txt'
    tag = ['日期', '时间', '最高价', '最低价', '成交量']

    with open(stock_file, mode='r', encoding='utf-8') as f:
        for line in f:
            row_stock_data.append(line.replace('\t', ' ').strip())

    with open(stock_day_file, mode='r', encoding='utf-8') as f:
        for line in f:
            row_stock_day_data.append(line.replace('\t', ' ').strip())

    # print(row_stock_data)
    # print(row_stock_day_data)
    return row_stock_data, row_stock_day_data


# 预处理股票数据
def pre_processing_stock(row_stock_data=None, row_day_data=None):
    if not row_data or not row_day_data:
        return

    all_stock_data=[]
    for item in row_data:
        data = []
        data_list = item.split(' ')
        data.append(data_list[0])
        data += data_list[1].split(',')

        all_data.append(data)

    return all_data


# 从csv文件读入数据
def load_from_csv(csv_file=None):
    if not csv_file:
        return
    csv_data = pd.read_csv(csv_file, index_col=0)  #防止弹出警告
    # print(csv_data)
    df = pd.DataFrame(csv_data)
    # print(type(df.values))   #numpy数组
    # print(df.values.tolist())
    return


# 将数据存入csv文件
def save_in_csv(all_data=None, tag=None, csv_file=None):
    if not all_data or not tag or not csv_file:
        return

    df = DataFrame(data=all_data, columns=tag)
    df.to_csv(path_or_buf=csv_file, encoding='utf-8', index_label=False)


# 预处理股票日数据
def pre_processing_day_data(stock_info=None, row_data=None):
    if not row_data or not stock_info:
        return

    all_data=[]
    for item in row_data:
        data = []
        data_list = item.split(' ')
        # 取出日期, 收盘价, 涨跌幅
        for i in range(0, 3):
            data.append(data_list[i])

        all_data.append(data)

    return all_data


# 将股票日数据存入csv文件
def save_day_data_in_csv(all_data=None, tag=None, csv_file=None):
    if not all_data or not tag or not csv_file:
        return

    df = DataFrame(data=all_data, columns=tag)
    df.to_csv(path_or_buf=csv_file, encoding='utf-8', index_label=False)


# 从csv文件读出股票日数据
def load_from_day_csv(file):

    pass


# 测试
if __name__ == '__main__':
    csv_day_file = './stock_day_data.csv'
    stock_tag = ['股票序号', '股票代码', '股票名称', '相关链接', '市盈率(动态)', '市净率']
    day_tag = ['日期', '收盘价', '涨跌幅']
    stock_info = ['21', '688390', '固德威']

    row_data, row_day_data = load_test_data()
    day_data = pre_processing_day_data(stock_info, row_day_data)
    print(day_data)

    # all_data = pre_processing_stock(row_data)
    # save_in_csv(all_data, tag, csv_file)
    # load_from_csv(csv_file)

