# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Shishao_Zhao"


'''
将从爬虫获取到的数据进行初步处理，
并存入csv文件
'''

# https://push2his.eastmoney.com/api/qt/stock/trends2/sse?fields1=f1&fields2=f53&secid=105.BILI&ndays=5

from datetime import datetime
from pandas import DataFrame


def pre_processing_stock(row_data):
    all_data=[]
    tag = ['日期', '时间', '最高价', '最低价', '成交量']
    row_data = ["2021-06-29 21:34,124.50,124.15,8304",
            "2021-06-29 21:35,124.83,124.43,10363",
            "2021-06-29 21:36,124.91,124.27,8743",
            "2021-06-29 21:37,124.90,124.33,5132",
            "2021-06-29 21:38,125.60,124.88,12862",
            "2021-06-29 21:39,125.67,125.30,10370",
            "2021-06-29 21:40,125.84,125.66,5494"]
    csv_path = './stock_dat.csv'
    for item in row_data:
        # print(item.split(' '))
        data1 = []
        data2 = {}
        l = item.split(' ')
        data1.append(l[0])
        data1 += l[1].split(',')
        # print(data)

        for i in range(0, 5):
            data2[tag[i]] = data1[i]
        # print(data2)
        all_data.append(data1)
        # print(data1)
        # print(tag)
        df = DataFrame(data=all_data, columns=tag)
        df.to_csv(path_or_buf=csv_path, encoding='utf-8-sig')
        pass
    # print(all_data)
    return all_data


def save_in_csv(all_data=None):
    pass


if __name__ == '__main__':
    fields1 = 'f1, f2, f3'
    fields2 = 'f53'
    url = 'https://push2his.eastmoney.com/api/qt/stock/trends2/sse?fields1=%s&fields2=%s&' \
          'secid=105.BILI&ndays=5' % (fields1, fields2)
    print(url)
    row_data = []
    pre_processing_stock(row_data)
    # save_in_csv()
    pass
