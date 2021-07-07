import csv
import glob
import random;
from pyecharts.faker import Faker;
from pyecharts import options as opts;
from pyecharts.charts import Bar, Grid, Line, Liquid, Tab, Pie
from pyecharts.globals import SymbolType
import numpy as np
import pandas as pd
import csv_util

filename = 'covid.csv'
all_files = glob.glob(filename)
all_data_file = []

cate = ["test preparation course", "math score", "reading score", "writing score", "sports score", "singing score",
        "sl score"]


def fake_fun():
    print(Faker.choose());
    print(Faker.values(1, 100));
    print(Faker.rand_color());
    print(list(z for z in zip(Faker.choose(), Faker.values(1, 100))));
    print(list((x, y, random.randint(1, 100)) for x in range(1, 10) for y in range(1, 10)));


def line_fun():
    c = (
        Line().add_xaxis(cate
                         ).add_yaxis(

            "线1", Faker.values(1, 100), itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color()),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")])
        ).add_yaxis(

            "线2", Faker.values(1, 100), itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color()),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")])
        ).set_global_opts(

            title_opts=opts.TitleOpts(title="stock", subtitle="linemap")
        )

    )
    return c


def bar_fun():
    c = (
        Bar().add_xaxis(cate
                        ).add_yaxis(
            # 添加 y 轴数据，并设置属性
            "柱1", Faker.values(1, 100), itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color())
        ).add_yaxis(
            # 添加 y 轴数据，并设置属性
            "柱2", Faker.values(1, 100), itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color())
        ).set_global_opts(
            # 设置图表属性
            title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


def pie_fun():
    # 数据格式[(key, value), (key, value), ...], 用 zip 函数将两个 list 进行组合
    data = [list(z) for z in zip(Faker.choose(), Faker.values())];
    c = (
        Pie().add(
                 series_name="",
                 data_pair=data,
                 rosetype="radius",
        ).set_global_opts(
        # 设置图表属性
                title_opts=opts.TitleOpts(title="主标题", subtitle="副标题")
        ).set_series_opts(
        # 设置 label 显示样式
                label_opts=opts.LabelOpts(
                formatter="{b}: {c}",
                color=Faker.rand_color(),
        )
      )
    )
    return c


def grid_mutil_yaxis():
    bar = (
        Bar()
            .add_xaxis(cate)
            .add_yaxis(
            "score",
            Faker.values(-300, 300), itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color()),
            yaxis_index=0,
            label_opts="inside"
        )
            .add_yaxis(
            "sub-score",
            Faker.values(-300, 300), itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color()),
            yaxis_index=1,
            label_opts="inside"
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                name="score",
                type_="value",
                min_=-300,
                max_=300,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color=Faker.rand_color())
                ),

            )
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                name="sub-score",
                type_="value",
                min_=-300,
                max_=300,
                position="right",
                offset=80,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color=Faker.rand_color())
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Grid-多 Y 轴示例"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )

    line = (
        Line()
            .add_xaxis(cate)
            .add_yaxis(
            "avarage-score",
            Faker.values(1, 10), itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color()),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min"), opts.MarkPointItem(type_="max")]),
            yaxis_index=2,
            label_opts=opts.LabelOpts(is_show=False),
        )
    )

    bar.overlap(line)
    return Grid().add(
        bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
        )


def liquid_fun():
    c = (
        Liquid()
            .add("lq", [0.3, 0.7], is_outline_show=False, shape=SymbolType.ARROW)
            .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-Shape-arrow"))
    )
    return c


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
            rosetype="radius",
        )
            .add(
            series_name="Milk Tea",
            data_pair=[],
            radius=60,
            center=["75%", "30%"],
            encode={"itemName": "product", "value": "2013"},
            rosetype="radius",
        )
            .add(
            series_name="Cheese Cocoa",
            data_pair=[],
            radius=60,
            center=["25%", "75%"],
            encode={"itemName": "product", "value": "2014"},
            rosetype="area",
        )
            .add(
            series_name="Walnut Brownie",
            data_pair=[],
            radius=60,
            center=["75%", "75%"],
            encode={"itemName": "product", "value": "2015"},
            rosetype="area",
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Dataset simple pie example"),
            legend_opts=opts.LegendOpts(pos_left="30%", pos_top="2%"),
        )
    )
    return c


def tab_fun():
    tab = Tab()
    tab.add(bar_fun(), "bar")
    tab.add(line_fun(), "line")
    tab.add(pie_fun(), "pie")
    tab.add(grid_mutil_yaxis(), "grid")
    tab.add(dataset_fun(),"dataset")
    tab.add(liquid_fun(),"liquidmap")
    tab.render("C:/Users/Administrator/Desktop/temp/tab.html")


if __name__ == "__main__":
    # fake_fun();
    # line_fun()
    # bar_fun()
    # pie_fun();
    # liquid_fun()
    # dataset_fun()
    # grid_mutil_yaxis()
    tab_fun()
