# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Shishao_Zhao"


'''
从爬虫获取到的数据进行初步处理，
存入csv文件
从csv文件读取
'''

from pandas import DataFrame
import pandas as pd
from spider.stockDailySpider import stockDailySpider


# 读测试数据
def load_test_data():
    row_stock_day_data = []
    stock_day_file = './stock_day.txt'

    with open(stock_day_file, mode='r', encoding='utf-8') as f:
        for line in f:
            row_stock_day_data.append(line.strip().split(','))

    # print(row_stock_day_data)
    return row_stock_day_data


# 预处理股票日数据
def pre_processing_data(row_data=None):
    if not row_data:
        return

    all_data = []
    for item in row_data:
        if not item:
            continue

        data = []
        l = item.split(',')
        # 取出日期(0), 收盘价(-4), 涨跌幅(-3)
        data.append(l[0])
        data.append(l[-4])
        data.append(l[-3])

        all_data.append(data)

    return all_data


# 将股票日数据存入csv文件
def save_data_in_csv(all_data=None, tag=None, stock_name=None):
    if not all_data or not tag or not stock_name:
        return

    csv_file = './%s.csv' % (stock_name)
    df = DataFrame(data=all_data, columns=tag)
    df.to_csv(path_or_buf=csv_file, encoding='utf-8', index_label=False)


# 从csv文件读出股票日数据，并返回一个字典
def load_from_csv(csv_file=None):
    if not csv_file:
        return
    csv_data = pd.read_csv(csv_file, index_col=0)
    df = pd.DataFrame(csv_data)
    data = df.to_dict(orient='list')

    return data


# 测试
if __name__ == '__main__':
    csv_day_file = './stock_day_data.csv'
    day_tag = ['日期', '收盘价', '涨跌幅']

    spider = stockDailySpider()
    stock_name, row_day_data = spider.run()
    day_data = pre_processing_data(row_day_data)
    save_data_in_csv(day_data, day_tag, stock_name)
    data = load_from_csv(stock_name + '.csv')


