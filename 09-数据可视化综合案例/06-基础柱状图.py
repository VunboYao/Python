from pyecharts.charts import Bar
from pyecharts.options import *

b = (
    Bar()
    .add_xaxis(['China', 'America', 'England'])
    .add_yaxis('GDP', [40, 80, 60])
    .set_global_opts(
        xaxis_opts=AxisOpts(
            splitline_opts=SplitLineOpts(is_show=False),
        ),
        yaxis_opts=AxisOpts(
            splitline_opts=SplitLineOpts(is_show=False),
            axisline_opts=AxisLineOpts(is_show=True)
        )
    )
    .render('Bar.html')
)
