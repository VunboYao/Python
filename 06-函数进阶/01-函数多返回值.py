"""
按照返回值的顺序，写对应顺序的多个变量接收即可
变量之间用逗号隔开
支持不同类型的数据return

多返回值的类型是 tuple
"""


def test_runner():
    return 1, 2


(x, y) = test_runner()

print(f'x is {x}, y is {y}')
