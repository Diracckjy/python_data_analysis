from pyecharts.faker import Faker;
from pyecharts import options as opts;
from pyecharts.charts import Bar, Grid, Line, Tab, Pie, Timeline
from pyecharts.globals import ThemeType
from csv_util import stock_csv

tl = Timeline()


def line_bar_fun(dict_x, dict_y1, dict_y2, stock_name):
    c = (
        Line({"theme": ThemeType.MACARONS}).add_xaxis(dict_x
                                                      ).add_yaxis(
            "收盘价", dict_y1, itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color()),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            is_smooth=True
        ).add_yaxis(

            "涨跌幅", dict_y2, itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color()),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            is_smooth=True
        ).set_global_opts(
            datazoom_opts=[opts.DataZoomOpts(type_="inside")],
            title_opts=opts.TitleOpts(title="线状-柱状图", subtitle=stock_name+"公司股票分析")
        )
    )
    b = (
        Bar({"theme": ThemeType.MACARONS}).add_xaxis(dict_x
                                                     ).add_yaxis(
            # 添加 y 轴数据，并设置属性
            "收盘价", dict_y1, itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color())
        ).add_yaxis(
            # 添加 y 轴数据，并设置属性
            "涨跌幅", dict_y2, itemstyle_opts=opts.ItemStyleOpts(color=Faker.rand_color())
        ).set_global_opts(
            # 设置图表属性
            datazoom_opts=[opts.DataZoomOpts(type_="inside")],
        )
    )
    grid = (
        Grid()
            .add(c, grid_opts=opts.GridOpts(pos_bottom="60%"))
            .add(b, grid_opts=opts.GridOpts(pos_top="60%"))

    )
    return grid


def pie_fun(dict_pie):
    # 数据格式[(key, value), (key, value), ...], 用 zip 函数将两个 list 进行组合
    data1 = [list(z) for z in zip(dict_pie[0], dict_pie[1])]
    data2 = [list(z) for z in zip(dict_pie[2], dict_pie[3])]
    data3 = [list(z) for z in zip(dict_pie[4], dict_pie[5])]
    data4 = [list(z) for z in zip(dict_pie[6], dict_pie[7])]
    pie1 = (
        Pie()
            .add(
            "",
            data1,
            rosetype="radius",
            radius=["50%", "70%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        ).set_global_opts(
            # 设置图表属性
            title_opts=opts.TitleOpts(title="饼状图", subtitle="公司01日股票分析"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
        ).set_series_opts(
            # 设置 label 显示样式
            label_opts=opts.LabelOpts(
                formatter="{b}: {c}",
                color=Faker.rand_color(),
            )
        )
    )
    pie2 = (
        Pie()
            .add(
            "",
            data2,
            rosetype="radius",
            radius=["50%", "70%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        ).set_global_opts(
            # 设置图表属性
            title_opts=opts.TitleOpts(title="饼状图", subtitle="公司01日股票分析"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
        ).set_series_opts(
            # 设置 label 显示样式
            label_opts=opts.LabelOpts(
                formatter="{b}: {c}",
                color=Faker.rand_color(),
            )
        )
    )
    pie3 = (
        Pie()
            .add(
            "",
            data3,
            rosetype="radius",
            radius=["50%", "70%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        ).set_global_opts(
            # 设置图表属性
            title_opts=opts.TitleOpts(title="饼状图", subtitle="公司03日股票分析"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
        ).set_series_opts(
            # 设置 label 显示样式
            label_opts=opts.LabelOpts(
                formatter="{b}: {c}",
                color=Faker.rand_color(),
            )
        )
    )
    pie4 = (
        Pie()
            .add(
            "",
            data4,
            rosetype="radius",
            radius=["50%", "70%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        ).set_global_opts(
            # 设置图表属性
            title_opts=opts.TitleOpts(title="饼状图", subtitle="公司04日股票分析"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
        ).set_series_opts(
            # 设置 label 显示样式
            label_opts=opts.LabelOpts(
                formatter="{b}: {c}",
                color=Faker.rand_color(),
            )
        )
    )
    tl.add(pie1, "01日")
    tl.add(pie2, "02日")
    tl.add(pie3, "03日")
    tl.add(pie4, "04日")
    return tl


def grid_mutil_yaxis(dict_x, dict_y1, dict_y2, stock_name):
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
            title_opts=opts.TitleOpts(title="Grid综合图-"+stock_name+"当日股票走势"),
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
            is_smooth=True
        )
    )

    bar.overlap(line)
    return Grid().add(
        bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
    )


def tab_fun(dictf, dicp, stock_name):
    tab = Tab()
    tab.add(line_bar_fun(dictf[0], dictf[1], dictf[2], stock_name), "line")
    tab.add(pie_fun(dicp), "pie")
    tab.add(grid_mutil_yaxis(dictf[0], dictf[1], dictf[2], stock_name), "grid")
    tab.render("tab.html")


def Init_map(csv_file, base_folder, stock_name):
    dict_tag = {}
    dict = stock_csv.load_from_csv(csv_file)
    dict_tag[0] = dict["日期"]
    dict_tag[1] = dict["收盘价"]
    dict_tag[2] = dict["涨跌幅"]

    dict_sumpie = {0: stock_csv.load_date_from_csv("2021-03-02", base_folder),
                   1: stock_csv.load_date_from_csv("2021-03-03", base_folder),
                   2: stock_csv.load_date_from_csv("2021-03-04", base_folder),
                   3: stock_csv.load_date_from_csv("2021-03-05", base_folder)}
    dict_pie = {0: dict_sumpie[0][0], 1: dict_sumpie[0][1], 2: dict_sumpie[1][0], 3: dict_sumpie[1][1],
                4: dict_sumpie[2][0], 5: dict_sumpie[2][1], 6: dict_sumpie[3][0], 7: dict_sumpie[3][1], }
    tab_fun(dict_tag, dict_pie, stock_name)


if __name__ == "__main__":
    csv_file = '../csv_data/三达膜.csv'
    Init_map(csv_file)
