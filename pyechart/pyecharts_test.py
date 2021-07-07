import random;
from pyecharts.faker import Faker;
from pyecharts import options as opts;
from pyecharts.charts import Bar, Bar3D, Line, Line3D, Pie;
from pyecharts.charts import Liquid
from pyecharts.globals import SymbolType
import numpy as np
import pandas as pd
import csv

def csv_read():
    csv_data = pd.read_csv('C:/Users/Administrator/Desktop/covid.csv')
    print(csv_data.shape)
    csv_batch_data = csv_data(5)
    print(csv_batch_data)




def fake_fun():
    print(Faker.choose());
    print(Faker.values(1, 100));
    print(Faker.rand_color());
    print(list(z for z in zip(Faker.choose(), Faker.values(1, 100))));
    print(list((x, y, random.randint(1, 100)) for x in range(1, 10) for y in range(1, 10)));

def line_fun():
    Line().add_xaxis(
        # 添加 x 轴数据
        Faker.choose()
    ).add_yaxis(
        # 添加 y 轴数据，并设置属性
        "线1", Faker.values(1, 100), itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color())
    ).add_yaxis(
        # 添加 y 轴数据，并设置属性
        "线2", Faker.values(1, 100), itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color())
    ).set_global_opts(
        # 设置图表属性
        title_opts=opts.TitleOpts(title="主标题", subtitle="副标题")
    ).render(
        # 设置输出路径
        path="C:/Users/Administrator/Desktop/temp/line.html"
    );

# 柱状图
def bar_fun():
    Bar().add_xaxis(
        # 添加 x 轴数据
        Faker.choose()
    ).add_yaxis(
        # 添加 y 轴数据，并设置属性
        "柱1", Faker.values(1, 100), itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color())
    ).add_yaxis(
        # 添加 y 轴数据，并设置属性
        "柱2", Faker.values(1, 100), itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color())
    ).set_global_opts(
        # 设置图表属性
        title_opts=opts.TitleOpts(title="主标题", subtitle="副标题")
    ).render(
        # 设置输出路径
        path="C:/Users/Administrator/Desktop/temp/bar.html"
    );

# 饼图
def pie_fun():
    # 数据格式[(key, value), (key, value), ...], 用 zip 函数将两个 list 进行组合
    data =  [list(z) for z in zip(Faker.choose(), Faker.values())];
    Pie().add(
        series_name="",
        data_pair=data,
    ).set_global_opts(
        # 设置图表属性
        title_opts=opts.TitleOpts(title="主标题", subtitle="副标题")
    ).set_series_opts(
        # 设置 label 显示样式
        label_opts=opts.LabelOpts(
            formatter="{b}: {c}",
            color=Faker.rand_color(),
        )
    ).render(
        # 设置输出路径
        path="C:/Users/Administrator/Desktop/temp/pie.html"
    );
def liquid_fun():
    c = (
        Liquid()
            .add("lq", [0.3, 0.7], is_outline_show=False, shape=SymbolType.ARROW)
            .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-Shape-arrow"))
            .render("C:/Users/Administrator/Desktop/temp/liquid_shape_arrow.html")
    )
def dataset_fun():
    c = (
        Pie()
            .add_dataset(
            source=[
                ["product", "2012", "2013", "2014", "2015", "2016", "2017"],
                ["Matcha Latte", 41.1, 30.4, 65.1, 53.3, 83.8, 98.7],
                ["Milk Tea", 86.5, 92.1, 85.7, 83.1, 73.4, 55.1],
                ["Cheese Cocoa", 24.1, 67.2, 79.5, 86.4, 65.2, 82.5],
                ["Walnut Brownie", 55.2, 67.1, 69.2, 72.4, 53.9, 39.1],
            ]
        )
            .add(
            series_name="Matcha Latte",
            data_pair=[],
            radius=60,
            center=["25%", "30%"],
            encode={"itemName": "product", "value": "2012"},
        )
            .add(
            series_name="Milk Tea",
            data_pair=[],
            radius=60,
            center=["75%", "30%"],
            encode={"itemName": "product", "value": "2013"},
        )
            .add(
            series_name="Cheese Cocoa",
            data_pair=[],
            radius=60,
            center=["25%", "75%"],
            encode={"itemName": "product", "value": "2014"},
        )
            .add(
            series_name="Walnut Brownie",
            data_pair=[],
            radius=60,
            center=["75%", "75%"],
            encode={"itemName": "product", "value": "2015"},
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Dataset simple pie example"),
            legend_opts=opts.LegendOpts(pos_left="30%", pos_top="2%"),
        )
            .render("C:/Users/Administrator/Desktop/temp/dataset_pie.html")
    )


if __name__ == "__main__":
     #fake_fun();
     #line_fun();
     #bar_fun();
     #pie_fun();
     #liquid_fun()
     #dataset_fun();
     csv_read()
