"""
pip3 install pyecharts

set_global_opts: 全局配置项
"""

# import
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, TooltipOpts

# instance
line = Line()

# add data
line.add_xaxis(['China', 'America', 'England'])
line.add_yaxis('GDP Data', [50, 30, 10])

# config
line.set_global_opts(
    title_opts=TitleOpts(title='Python Basic', pos_left='center', pos_bottom='1%'),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True)
)

# render
line.render()
