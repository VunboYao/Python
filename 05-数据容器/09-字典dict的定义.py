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

my_dict['sex'] = 'male'

# 删除
res = my_dict.pop('score')

print(my_dict, 'res =>', res)

# 清空
# my_dict.clear()
print(my_dict)

# keys
keys = my_dict.keys()
print(keys)

# for + keys
for key in my_dict.keys():
    print(f'{key}:{my_dict[key]}')

# 直接遍历，拿到的就是key值
for key in my_dict:
    print(key)