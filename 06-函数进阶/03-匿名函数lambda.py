# 函数参数
def func(computed):
    result = computed(1, 2)
    print(result)


def add(x, y):
    return x + y


func(add)


"""
lambda匿名函数
    - def 关键字，定义带有名称的函数
    - lambda关键字，定义匿名函数
    - 匿名函数只可临时使用一次
语法：lambda 参数列表：函数体(一行代码)
    - lambda 是关键字，表示定义匿名函数
    - 传入参数表示匿名函数的形参。如:x, y表示接受2个形参
    - 函数体，函数的执行逻辑，注意：只能写一行，无法写多行代码
"""


def func(calculate):
    result = calculate(1, 2)
    print(f'result is {result}')


func(lambda x, y: x * y)
