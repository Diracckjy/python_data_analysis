# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Shishao_Zhao"


'''
将从爬虫获取到的数据进行初步处理，
并存入csv文件
'''

from pandas import DataFrame


# 预处理数据
def pre_processing_stock(row_data=None):
    if not row_data:
        return

    all_data=[]
    for item in row_data:
        data = []
        data_list = item.split(' ')
        data.append(data_list[0])
        data += data_list[1].split(',')

        all_data.append(data)

    return all_data


# 将数据存入csv文件
def save_in_csv(all_data=None, tag=None):
    if not all_data or not tag:
        return

    csv_path = './stock_dat.csv'
    df = DataFrame(data=all_data, columns=tag)
    df.to_csv(path_or_buf=csv_path, encoding='utf-8')


# 测试
if __name__ == '__main__':
    row_data = ["2021-06-29 21:34,124.50,124.15,8304",
                "2021-06-29 21:35,124.83,124.43,10363",
                "2021-06-29 21:36,124.91,124.27,8743",
                "2021-06-29 21:37,124.90,124.33,5132",
                "2021-06-29 21:38,125.60,124.88,12862",
                "2021-06-29 21:39,125.67,125.30,10370",
                "2021-06-29 21:40,125.84,125.66,5494"]
    tag = ['日期', '时间', '最高价', '最低价', '成交量']
    all_data = pre_processing_stock(row_data)
    save_in_csv(all_data, tag)
    pass
