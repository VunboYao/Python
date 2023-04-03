from pyecharts.charts import Timeline, Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取数据
with open('1960-2019GDP.csv', 'r', encoding='GB2312') as f:
    data = f.readlines()
    data.pop(0)

dict_data = {}
# 遍历数据，拼接需要的数据
for item in data:
    # 将每一行分割
    line_data = item.split(',')
    # 获取年份
    dict_key = int(line_data[0])
    # 将最后的金额转为浮点数，同时会自动将换行符移除
    str_to_num = float(line_data[-1])

    # 以年份为key,将每个国家和gdp放到一个元组中，并append到年份的value中
    if dict_key in dict_data:
        dict_data[dict_key].append((line_data[1], str_to_num))
    else:
        dict_data[dict_key] = []
        dict_data[dict_key].append((line_data[1], str_to_num))
# {
#   1960:[(china, 1231231), (india, 123132), (usa, 99999), ...],
#   1961:[...]
# }

# 创建时间线，并设置主题
time_line = Timeline(init_opts=InitOpts(
    theme=ThemeType.LIGHT
))

# 对年份的数据进行排序[1961, 1962, 1963,...]
list_keys = sorted(dict_data.keys())
# 遍历年份
for year in list_keys:
    # 对每一年的数据，比较其GDP，reverse从大到小展示.【sort方法改变自身】
    dict_data[year].sort(key=lambda el: el[1], reverse=True)
    year_data = dict_data[year][0:8]
    # 反转每年的数据，前8从小到大展示
    year_data.reverse()

    # x轴年份信息
    country = []
    # y轴GDP信息
    gdp_list = []

    # 遍历这8条数据，拼接出x轴与y轴的数据
    for item in year_data:
        country.append(item[0])
        # 亿为单位
        gdp_list.append(int(item[1] / 100000000))

    # 根据每一年的，前8个国家的GDP构建Bar图
    b = (
        Bar()
        # x轴数据，国家列表[英国，美国，法国，西班牙...]
        .add_xaxis(country)
        # y轴数据，GDP
        .add_yaxis('GDP(亿)', gdp_list, label_opts=LabelOpts(position='inside', color='white'))
        # 反转
        .reversal_axis()
        # 设置全局配置，标题信息
        .set_global_opts(
            title_opts=TitleOpts(title=f'{year}年全球前8 GDP国家'),
            xaxis_opts=AxisOpts(
                splitline_opts=SplitLineOpts(is_show=False),
                axisline_opts=AxisLineOpts(is_show=True)
            ),
            yaxis_opts=AxisOpts(
                splitline_opts=SplitLineOpts(is_show=False),
                axisline_opts=AxisLineOpts(is_show=True)
            ),
            tooltip_opts=TooltipOpts(is_show=True),
            toolbox_opts=ToolboxOpts(is_show=True)
        )
    )

    # 时间线添加一个bar
    time_line.add(b, str(year))

time_line.add_schema(
    play_interval=1000,
    is_auto_play=True,
    is_loop_play=False
)
time_line.render('1960-2019全球GDP前8国家.html')
