"""
查询：
    查询索引:list.index(元素), 没有则报错Error
    统计某元素在列表中的数量 list.count(元素)
    长度获取：length = len(list)
修改：
    修改某个下标的值: list[0]='value'
    插入元素：list.insert(下标，元素)
    追加元素：list.append(元素)
    追加批量元素：list.extend(new_list)
删除
    del list[index]
    res = list.pop(index) 默认索引为-1
    list.remove(元素）删除找到的第一个元素
清空列表
    list.clear()
"""

name_list = ['Emma', 'Anna', 'Duo', 'Lili', ('Vunbo', 'Yao'), True, 2, ['Ben', 'July']]

# index(item)
print(f'查询list中2的索引：{name_list.index(2)}')

# 修改,支持反向下标
name_list[0] = 'Yao'
print(f'根据索引0修改list中的数据：{name_list}')

# insert
name_list.insert(1, 'Vunbo')
print(f'list中索引1处insert插入数据Vunbo：{name_list}')

# append
name_list.append('UK')
print(f'list中append追加元素UK：{name_list}')

# extend
new_list = ['Australia', 'Duo']
name_list.extend(new_list)
print(f'list中extend批量追加元素：{name_list}')

# del
del name_list[5]
print(f'通过del list[5]方式删除数据:{name_list}')

# pop
res = name_list.pop(7)
print(f'通过list.pop(7)方式删除数据，返回删除的值{res} => list为：{name_list}')

# remove
name_list.remove('Yao')
print(f'通过list.remove(“yao”)删除匹配到的第一个元素：{name_list}')

# 统计某个元素的数量
count = name_list.count('Duo')
print(f'通过list.count("Duo")统计数量,{count}个Duo')

print(f'通过len获取长度:{len(name_list)}')

# clear
name_list.clear()
print(f'list.clear清空列表数据:{name_list}')