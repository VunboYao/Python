"""
字符串格式化语法
    "%占位符" % 变量

常用的占位符
    字符串： %s
    整数：   %d
    浮点数：  %f

"""

first_name = 'Vunbo'
last_name = 'Yao'
number = 666

# 占位的形式：%s
message = "My fullname is %s%s, and my score is %s" % (first_name, last_name, number)
print(message)

name = 'Vunbo'
age = 20
number = 20.99
message = "name: %s, age: %d, score: %f" % (name, age, number)
print(message)
