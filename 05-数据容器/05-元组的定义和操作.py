"""
元组：一旦定义完成，不可修改
    使用小括号定义，逗号隔开，数据是可以不同的数据类型
    (x, y, z ...)
    变量名称 = ()
    变量名称 = tuple()
"""

# 定义元组
t1 = (1, 'Hello', True)
t2 = ()
t3 = tuple()

# 定义单个元素的元组，需要在后边增加括号
t4 = ('hello',)
print(f't4的type是{type(t4)}')

# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f't5的type是{type(t5)}')

# 索引取出内容
num = t5[1][2]
print(f'从嵌套元组中获取的数据是{num}')

# 元组的操作：index 查找方法
t6 = ('Hello', 'Vunbo', 'Yao')
index = t6.index('Yao')
print(f'在t6中查找Yao的索引:{index}')

# 元组的操作：count 统计方法
t7 = ('Hello', 'Vunbo', 'Yao', 'Yao', 'Yao')
count = t7.count('Yao')
print(f'在t7中查找Yao的数量:{count}')

# 元组的操作：len函数统计元组元素的数量
t8 = ('Hello', 'Vunbo', 'Yao', 'Yao', 'Yao')
count = len(t8)
print(f't8中共有{count}个元组')

# while
index = 0
while index < len(t8):
    print(f'while: 元组的元素有{t8[index]}')
    index += 1

# for
for i in t8:
    print(f'for: 元组的元素有 {i}')

# 元组中的引用数据可修改
t9 = (1, 2, ['Hello', 'World'])
t9[2][1] = 'Python'
print(f't9的值现在是{t9}')
