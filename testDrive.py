from pyechart.pyecharts_test import Init_map
from csv_util.stock_csv import pre_processing_data, save_data_in_csv, load_from_csv
from spider.stockDailySpider import stockDailySpider
import os

# 主测试函数
if __name__ == '__main__':
    tag = ['日期', '收盘价', '涨跌幅']
    base_folder = 'csv_data/'

    # 创建爬虫
    spider = stockDailySpider()

    # 爬取数据
    stock_name, row_day_data = spider.run()
    if stock_name is None:
        exit(0)

    # 数据预处理
    day_data = pre_processing_data(row_day_data)

    # 将数据存入csv文件
    save_data_in_csv(day_data, tag, stock_name, base_folder)

    # 将数据存入mysql

    # 从csv文件读出数据
    # data = load_from_csv(stock_name + '.csv')

    # 生成日数据柱状、折线图和生成数据饼图
    csv_file = base_folder + stock_name + '.csv'
    Init_map(csv_file, base_folder, stock_name)
