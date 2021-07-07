import glob
import random;
from pyecharts.faker import Faker;
from pyecharts import options as opts;
from pyecharts.charts import Bar, Grid, Line, Liquid, Tab, Pie, Kline
from pyecharts.globals import SymbolType
from pyecharts.globals import ThemeType
from csv_util import stock_csv

dict_x = []
dict_y1 = []
dict_y2 = []
dict_pie1 = []
dict_pie2 = []

def line_fun():
    c = (
        Line().add_xaxis(dict_x
                         ).add_yaxis(

            "收盘价", dict_y1, itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color()),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5)
        ).add_yaxis(

            "涨跌幅",dict_y2, itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color()),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5)
        ).set_global_opts(
            datazoom_opts=[opts.DataZoomOpts(type_="inside")],
            title_opts=opts.TitleOpts(title="线状图", subtitle="公司股票分析")
        )

    )
    return c


def bar_fun():
    c = (
        Bar({"theme": ThemeType.MACARONS}).add_xaxis(dict_x
                                                     ).add_yaxis(
            # 添加 y 轴数据，并设置属性
            "收盘价", dict_y1, itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color())
        ).add_yaxis(
            # 添加 y 轴数据，并设置属性
            "涨跌幅", dict_y2, itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color())
        ).set_global_opts(
            # 设置图表属性
            title_opts=opts.TitleOpts(title="柱状图", subtitle="公司股票分析"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


def pie_fun():
    # 数据格式[(key, value), (key, value), ...], 用 zip 函数将两个 list 进行组合
    data = [list(z) for z in zip(dict_pie1, dict_pie2)];
    c = (
        Pie().add(
            series_name="",
            data_pair=data,
            rosetype="radius",
        ).set_global_opts(
            # 设置图表属性
            title_opts=opts.TitleOpts(title="饼状图", subtitle="公司股票分析")
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
        Bar(init_opts=opts.InitOpts(width="1680px", height="800px"))
            .add_xaxis(dict_x)
            .add_yaxis(
            "收盘价",
            dict_y1, category_gap="0%", itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color()),
            yaxis_index=1,
        )
            .add_yaxis(
            "涨跌幅",
            dict_y2, category_gap="0%", itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color()),
            yaxis_index=2,
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                name="收盘价",
                type_="value",
                position="right",
                max_=270,
                min_=-200,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color=Faker.rand_color())
                ),

            )
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                name="涨跌幅",
                type_="value",
                position="right",
                offset=80,
                max_=20,
                min_=-20,
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
            title_opts=opts.TitleOpts(title="Grid综合图-三孚新科当日股票走势"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(orient="vertical")],
            toolbox_opts=opts.ToolboxOpts(pos_left="820"),

        )

    )

    line = (
        Line()
            .add_xaxis(dict_x)
            .add_yaxis(
            "跌涨幅趋势",
            dict_y1, itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color()),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min"), opts.MarkPointItem(type_="max")]),
            yaxis_index=0,
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


def kmap_fun():
    c = (
        Kline()
            .add_xaxis(["2017/7/{}".format(i + 1) for i in range(31)])
            .add_yaxis("kline", )
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(is_scale=True),
            yaxis_opts=opts.AxisOpts(
                is_scale=True,
                splitarea_opts=opts.SplitAreaOpts(
                    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                ),
            ),
            datazoom_opts=[opts.DataZoomOpts()],
            title_opts=opts.TitleOpts(title="Kline-DataZoom-slider"),
        )
    )
    return c


def tab_fun():
    tab = Tab()
    tab.add(bar_fun(), "bar")
    tab.add(line_fun(), "line")
    tab.add(pie_fun(), "pie")
    tab.add(grid_mutil_yaxis(), "grid")
    tab.add(dataset_fun(), "dataset")
    tab.add(liquid_fun(), "liquidmap")
    # tab.add(kmap_fun(),"k-line")
    tab.render("C:/Users/Administrator/Desktop/temp/tab.html")


if __name__ == "__main__":
    dict = stock_csv.load_from_csv("../csv_data/三孚新科.csv")
    dict2 = stock_csv.load_date_from_csv("2021-07-07")
    dict_x = dict["日期"]
    dict_y1 = dict["收盘价"]
    dict_y2 = dict["涨跌幅"]
    dict_pie1 = dict2[0]
    dict_pie2 = dict2[1]
    tab_fun()
