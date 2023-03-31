"""
列表：
    - 以[]作为标识
    - 列表内每一个元素之间用逗号(，)隔开
    - [item1, item2, item3, ...]

定义空列表：
    变量 = []
    变量 = list()

注意：
    - 列表可以一次存储多个数据，且可以为不同的数据类型，支持嵌套
"""

name_list = ['Emma', 'Anna', 'Duo', 'Lili', ('Vunbo', 'Yao'), True, 2, []]

for i in name_list:
    print(f'{i} 的类型是 {type(i)}')
