"""
1. import json
2. python data => json: json.dumps(data)
    2.1 如果有中文要展示：ensure_ascii=False 参数来确保中文正常转换
3. json => python data: json.loads(data)
"""

import json

# type is dict
dict_data = {"name": "你好", "age": 18}
# type is list
list_data = [{"name": "admin", "age": 18}, {"name": "root", "age": 16}, {"name": "张三", "age": 20}]
print(type(dict_data), type(list_data))

# dict => json
json_dict = json.dumps(dict_data, ensure_ascii=False)
print(f'json_data的数据类型是: {type(json_dict), json_dict}')  # str

# json => dict
json = json.loads(json_dict)
print(f'list_data的数据类型是: {type(dict_data)}')  # dict
