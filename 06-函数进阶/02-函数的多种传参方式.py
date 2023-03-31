"""
4种常见的参数使用方式：
    - 位置参数
        - 传递的参数和定义的参数的顺序及个数必须一致
    - 关键字参数
        - 函数调用时通过“键=值”形式传递参数
        - 可以让函数更加清晰、容易使用，同时也清除了参数的顺序要求
        - 函数调用时，如果有位置参数，位置参数必须在关键字参数前面，但关键字参数之间不存在先后顺序
    - 缺省参数
        - 也叫默认参数。定义函数时，为参数提供默认值，调用函数时可不传该默认参数的值。
        - 所有位置参数必须出现在默认参数前，包括函数定义和调用
    - 不定长参数
        - 可变参数。用于不确定调用的时候会传递多少个参数的场景
        - 位置传递*args：所有的参数都被args变量收集，合并为一个元组(tuple)，args是元组类型
        - 关键字传递**kwargs: 参数是“键=值”形式的情况下，所有的“键=值”都会被kwargs接受，组成字典(dict)形式
"""


def user_info(name, age, modify, gender='male'):
    print(f'{modify} Your name is {name}, age is {age}, gender is {gender}')


# 位置参数
user_info('Yao', 29, gender='male', modify='位置参数默认使用：')

# 关键字参数
user_info(name='Yao', gender='Male', age=20, modify='关键字参数的使用：')
# 位置参数需要在关键字参数前面
user_info('Vunbo', gender='male', age=20, modify="位置参数需要在关键字参数前：")

# gender有默认值
user_info('Emma', 20, modify="默认参数使用：")


# 位置传递
def user_info(*args):
    # print(f'可变参数-位置传递：Name is {args[0]}, gender is {args[1]}, age is {args[2]}')
    name, gender, age = args
    print(f'可变参数-位置传递：Name is {name}, gender is {gender}, age is {age}')


user_info('Anna', 'female', 20)


# 关键字传递
def user_info(**kwargs):
    # print(type(kwargs))  # dict
    # print(f"可变参数-关键字传递：Name is {kwargs['name']}, age is {kwargs['age']}, gender is {kwargs['gender']}, score is {kwargs['score']}")
    print(f"可变参数-关键字传递：", end="")
    for key in kwargs:
        print(f"{key} is {kwargs[key]},", end="")


user_info(name='Duo', age=20, gender="male", score=100)