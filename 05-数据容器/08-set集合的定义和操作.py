"""
list: []
tuple: ()
str: ""
set: {a,b} 去重且无序
    set.add(item)
    set.remove(item)
    set.pop()
    set.clear()
    set.difference(set2)： 返回一个新的集合，set有，set2没有的
    set.difference_update(set2)：删除集合1中和集合2中相同的元素，集合1变化，集合2不变
    set.union(set2):得到一个新的集合，内涵2个集合的内部元素
    len(set)
    定义空集合 set()

    无序，不能重复，不支持while循环
"""

my_set = {'Hello', 'Yao', 'World', 'Hello', 'Yao', 'World', 'Hello', 'Yao', 'World'}
my_set_empty = set()
print(my_set)  # {'Hello', 'World', 'Yao'}
print(my_set_empty)  # set()

# add
my_set.add('Python')
print(f'新增一个元素：{my_set}')

# remove
my_set.remove('Yao')
print(f'移除Yao：{my_set}')

# pop
random_set = my_set.pop()
print(f'随机取出一个数: {random_set}')

# clear
my_set.clear()
print(f'clear all set: {my_set}')

# difference
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f'新的集合是{set3}')

# difference_update
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(f'集合1的值是{set1},集合2是{set2}')

# union
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f'集合后：\nset1:{set1}\nset2:{set2}\nset3:{set3}')

print('------------practice-----------')
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
print(set(my_list))
