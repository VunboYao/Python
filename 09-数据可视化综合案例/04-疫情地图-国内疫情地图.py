import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 读取数据
with open('yiqing.txt', 'r') as f:
    data = json.loads(f.read())

# 获取特定的字段
data = data['areaTree'][0]['children']
data_list = []

# 遍历数据，拼接需要的数据内容
for province_data in data:
    province_name = province_data['name'] + '省'
    province_value = province_data['total']['confirm']

    data_list.append((province_name, province_value))

# 定义map
m = (
    Map()
    .add('疫情地图', data_list, 'china')
    .set_global_opts(
        visualmap_opts=VisualMapOpts(
            is_piecewise=True,
            pieces=[
                {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
                {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
                {"min": 100, "max": 499, "label": "99-499人", "color": "#FF9966"},
                {"min": 500, "max": 999, "label": "499-999人", "color": "#FF6666"},
                {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
                {"min": 10000, "label": "10000以上", "color": "#990033"}
            ]
        )
    )
).render('疫情地图.html')
