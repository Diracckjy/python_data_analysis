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
from spider.stockGetDays import stockGetDays
from os import listdir
import os


# 预处理并存取多个股票数据
def save_multi_data_in_csv(all_data=None):
    if not all_data:
        return

    tag = ['日期', '收盘价', '涨跌幅']
    for data_dict in all_data:
        data = pre_processing_data(data_dict['data'])
        save_data_in_csv(data, tag, data_dict['name'])


# 预处理股票日数据, 取出日期, 收盘价和涨跌幅，舍弃无效数据
# 输入一个原始数据list
# 返回一个包含日期, 收盘价和涨跌幅的数据list
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
# 输入数据list, 标签list(日期, 收盘价和涨跌幅), 字符串股票名
# 无返回值
def save_data_in_csv(all_data=None, tag=None, stock_name=None, base_folder=None):
    if not all_data or not tag or not stock_name or not base_folder:
        return

    # csv_file = '../csv_data/%s.csv' % stock_name
    csv_file = base_folder + '%s.csv' % stock_name
    # print(os.getcwd())
    # print(os.path.exists(base_folder + '%s.csv'))
    df = DataFrame(data=all_data, columns=tag)
    df.to_csv(path_or_buf=csv_file, encoding='utf-8', index_label=False)


# 从csv文件读出股票日数据
# 输入文件名
# 返回一个字典，key为字段名, value为对应字段的列值
def load_from_csv(csv_file=None):
    if not csv_file:
        return
    csv_data = pd.read_csv(csv_file, index_col=0)
    df = pd.DataFrame(csv_data)
    data = df.to_dict(orient='list')

    return data


# 按日期取出csv_data文件夹中所有公司该日股票数据
# 输入日期格式YYYY-MM-DD
# 返回两个list，一个公司名称list，一个收盘价list
def load_date_from_csv(date=None, base_folder=None):
    if not date or not base_folder:
        return
    files = listdir(base_folder)      # 列出文件夹中所有文件
    cop_list, price_list = [], []
    for file in files:
        # print(file.split('.'))
        cop_list.append(file.split('.')[0])
        csv_data = pd.read_csv(base_folder+file, index_col=0)
        l = csv_data.values.tolist()
        for item in l:
            if date in item:
                price_list.append(item[1])       # 取出收盘价
                break       # 查询下一个item

    return cop_list, price_list


# 测试
if __name__ == '__main__':
    day_tag = ['日期', '收盘价', '涨跌幅']
    date = '2021-07-07'
    base_folder = './csv_data/'
    spider = stockDailySpider()
    # 爬取数据
    stock_name, row_day_data = spider.run()
    # 数据预处理
    day_data = pre_processing_data(row_day_data)
    # 将数据存入csv文件
    save_data_in_csv(day_data, day_tag, stock_name, base_folder)
    # # 从csv文件读出数据
    # data = load_from_csv(stock_name + '.csv')

    # load_date_from_csv(date)

    # 同时爬取多个公司数据
    # spider = stockGetDays()
    # all_data = spider.run()
    # save_multi_data_in_csv(all_data)


