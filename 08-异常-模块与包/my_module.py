"""
每个 Python 文件都可以作为一个模块，模块的名字就是文件的名字
    自定义模块名必须符号标识符命名规则
"""

# 当一个模块文件中有 "__all__"变量时，在使用`from xx import *`时，只能导入这个列表中的元素
__all__ = ['add']


def add(a, b):
    print(f'当前文件是: {__name__} => {a + b}')
    return a + b


def sub(a, b):
    print(f'my_module中sub方法的结果是:{a - b}')
    return a - b


# 只在当前文件中调用该函数时执行；其它导入的文件内不符合该条件，不执行测试函数的调用
if __name__ == '__main__':
    add(2, 5)
