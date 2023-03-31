
"""
def 函数名(参数)：
    函数体
    return 返回值

函数的调用：函数名(参数1，参数2，参数3)


None：NoneType类型，表示空、无意义的
    用作函数返回值
    主动声明一个变量为None
"""


def say_hi(a, b):
    print('Hello Python', a + b)
    return None


res = say_hi(4, 11)  # 无返回值，默认返回None
print(f'result is {res}, the type is {type(res)}')

