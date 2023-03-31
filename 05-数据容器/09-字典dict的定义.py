"""
 删除操作： res = dict.pop(key)
 清空：dict.clear()
 获取所有的key: res = dict.keys()
 长度获取：len(dict)
"""
my_dict = {
    "name": 'Yao',
    "age": 20,
    "score": 88
}
print(my_dict['name'])
print(my_dict['score'])

# 新增元素
my_dict['sex'] = 'male'
print(f'新增一个sex属性：{my_dict}')

# 删除
res = my_dict.pop('score')
print(f'删除属性score, 它的值是{res}, 原dict为：{my_dict}')

# 清空
my_dict.clear()
print(f'清空dict： {my_dict}')

# keys
my_dict = {
    "name": 'Yao',
    "age": 20,
    "score": 88
}
keys = my_dict.keys()
print(f'获取dict的key，返回的类型是:{type(keys)}, 数据是{keys}')

# for + keys
for key in my_dict.keys():
    print(f'for遍历：{key}:{my_dict[key]}')

# 直接遍历，拿到的就是key值
for key in my_dict:
    print(f'直接遍历dict,即可拿到key: {key}')
