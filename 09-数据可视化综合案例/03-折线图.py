import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, SplitLineOpts, LegendOpts, InitOpts, AxisOpts, LabelOpts, AxisLineOpts


def get_country_data(file_path):
    """
    根据传入的文件路径，读取内容，返回x, y 轴的坐标信息
    :param file_path: 文件路径
    :return: x, y 坐标数据
    """
    with open(file_path, 'r', encoding='UTF-8') as f:
        # 读取数据
        data = f.read()

        # 从左括号(后开始截取数据
        split_start = data.index('(') + 1
        # 最后2个字符串截取掉
        data = data[split_start:-2]

        # str => dict
        data = json.loads(data)

        data = data['data'][0]['trend']
        x_data = data['updateDate'][:314]
        y_data = data['list'][0]['data'][:314]

        return x_data, y_data


# 获取元组中的数据坐标
(india_x, india_y) = get_country_data('India.txt')
(usa_x, usa_y) = get_country_data('America.txt')
(japan_x, japan_y) = get_country_data('Japan.txt')

# 执行line的初始化配置
init_options = InitOpts(width="1600px", height="800px")
line = Line(init_options)

# x轴坐标
line.add_xaxis(usa_x)

# y轴数据与展示的label
line.add_yaxis('Japan', y_axis=japan_y, label_opts=LabelOpts(is_show=False))
line.add_yaxis('USA', y_axis=usa_y, label_opts=LabelOpts(is_show=False))
line.add_yaxis('India', y_axis=india_y, label_opts=LabelOpts(is_show=False))

# 全局配置，移除坐标网格背景
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美日印累计确诊人数对比图", pos_left='center'),
    xaxis_opts=AxisOpts(name="时间", splitline_opts=SplitLineOpts(is_show=False)),
    yaxis_opts=AxisOpts(name="累计确诊人数", splitline_opts=SplitLineOpts(is_show=False), axisline_opts=AxisLineOpts(is_show=True)),
    legend_opts=LegendOpts(pos_left='70%'),
)
line.render()
