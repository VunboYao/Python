"""
if 语句的基本格式

if 条件：
    条件成立时，doSomething

注意：
    4个空格缩进
    判断条件后的冒号
"""

age = 20

if age >= 18:
    print('I am an adult!')
    print('I can play the video game')

print('Done')

print('------practice------')

age = int(input('Please input your age:'))
if age >= 18:
    print('You are an adult, you need to cost 10')

print('Have a nice time!')
