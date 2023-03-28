"""
列表：
    以[]作为标识

定义空列表：
    变量 = []
    变量 = list()

下标索引：
    从0开始到length-1
反向索引：
    最后一个是-1
嵌套索引：
    xxx[2][1]
错误示范Error：
    下标获取数据，超出范围
"""

name_list = ['Emma', 'Anna', 'Duo', 'Lili', ('Vunbo', 'Yao'), True, 2, ['Ben', 'July']]

print(name_list[0])
print(name_list[3])
print(name_list[-1])

# 嵌套的索引
print(name_list[-1][1])
