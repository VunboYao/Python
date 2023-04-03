from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
# 主题设置
from pyecharts.globals import ThemeType

bar1 = (
    Bar()
    .add_xaxis(['America', 'China', 'England'])
    .add_yaxis('GDP', [40, 10, 20], label_opts=LabelOpts(position='inside'))
    .set_global_opts(
        xaxis_opts=AxisOpts(
            # 隐藏分割线
            splitline_opts=SplitLineOpts(is_show=False),
            # 展示x轴线
            axisline_opts=AxisLineOpts(is_show=True)
        ),
        yaxis_opts=AxisOpts(
            splitline_opts=SplitLineOpts(is_show=False),
            axisline_opts=AxisLineOpts(is_show=True)
        )
    )
    .reversal_axis()
)

bar2 = (
    Bar()
    .add_xaxis(['America', 'China', 'England'])
    .add_yaxis('GDP', [80, 40, 40], label_opts=LabelOpts(position='right'))
    .set_global_opts(
        xaxis_opts=AxisOpts(
            splitline_opts=SplitLineOpts(is_show=False),
            axisline_opts=AxisLineOpts(is_show=True)
        ),
        yaxis_opts=AxisOpts(
            splitline_opts=SplitLineOpts(is_show=False),
            axisline_opts=AxisLineOpts(is_show=True)
        )
    )
    .reversal_axis()
)

bar3 = (
    Bar()
    .add_xaxis(['America', 'China', 'England'])
    .add_yaxis('GDP', [180, 40, 90], label_opts=LabelOpts(position='right'))
    .set_global_opts(
        xaxis_opts=AxisOpts(
            splitline_opts=SplitLineOpts(is_show=False),
            axisline_opts=AxisLineOpts(is_show=True)
        ),
        yaxis_opts=AxisOpts(
            splitline_opts=SplitLineOpts(is_show=False),
            axisline_opts=AxisLineOpts(is_show=True)
        )
    )
    .reversal_axis()
)

timeline = (
    # 主题配置
    Timeline(init_opts=InitOpts(theme=ThemeType.ESSOS))
    .add(bar1, '2019年GDP')
    .add(bar2, '2020年GDP')
    .add(bar3, '2021年GDP')
    # timeline播放控制
    .add_schema(
        is_auto_play=True,
        is_loop_play=True,
        play_interval=2000,
        controlstyle_opts=TimelineControlStyle(
            position='right',
            color='red',
            border_width=2,
            border_color='red'
        )
    )
).render('timeline.html')
