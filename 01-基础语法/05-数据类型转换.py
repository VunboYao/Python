"""
    type(数据)，返回数据的类型
    int(x)：将 x 转换为一个整数
    float(x)：将 x 转换为一个浮点数
    str(x)：将对象 x 转换为字符串

注意：
    类型转换不是万能的
"""
print(type(666))  # int
print(type(13.14))  # float
print(type('Hello'))  # str
print(type(True))  # bool
print(type(4+3j))  # complex
print(type((12, 12)))  # tuple
print(type({}))  # dict
print(type(set([1, 3])))  # set

# 字符串转换成数字类型，必须是纯数字的字符串
tFoo = int('123')
print('str => int', type(tFoo), tFoo)

tStr = str(666)
print('int => str', type(tStr), tStr)

float_str = str(11.345)
print('float => str', type(float_str), float_str)

# 浮点数转整数，丢失精度
int_number = int(11.945)
print('float => int，丢失精度：', type(int_number), int_number)

float_number = float(12)
print('int => float', type(float_number), float_number)
