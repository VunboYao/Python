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

# print(name_list.index(2))
# print(name_list.index('Hello'))

name_list[0] = 'Yao'
# print(name_list)

name_list.insert(1, 'Vunbo')
# print(name_list)

name_list.append('UK')
# print(name_list)

new_list = ['Australia', 'Korean']
name_list.extend(new_list)
# print(name_list)

del name_list[5]
# print(name_list)
res = name_list.pop(7)
# print(res, name_list)

name_list.remove('Yao')
# print(name_list)

# name_list.clear()
# print(name_list)

count = name_list.count('Duo')
# print(count)

print(len(name_list))
