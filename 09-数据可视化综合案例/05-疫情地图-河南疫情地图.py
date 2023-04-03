import json
from pyecharts.charts import Map
from pyecharts.options import *


# 查询索引的方法
def find_index(outside_data, target):
    for item in enumerate(outside_data):
        if item[1]['name'] == target:
            return item[0]


# 读取数据
with open('yiqing.txt', 'r') as f:
    data = json.loads(f.read())

# 获取特定的字段
data = data['areaTree'][0]['children']
data_list = []

# 获取children中省份的索引
province_index = find_index(data, '广东')

# 获取相关城市
city_data = data[province_index]['children']

for city in city_data:
    city_name = city['name'] + '市'
    city_confirm = city['total']['confirm']
    data_list.append((city_name, city_confirm))

data_list.append(('云浮市', 1000))

# 定义map
m = (
    Map()
    .add('广东疫情地图', data_list, '广东')
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
).render('广东疫情地图.html')
