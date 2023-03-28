"""
列表：
    以[]作为标识

定义空列表：
    变量 = []
    变量 = list()
"""

name_list = ['Emma', 'Anna', 'Duo', 'Lili', ('Vunbo', 'Yao'), True, 2, []]

for i in name_list:
    print(f'{i} 的类型是 {type(i)}')
