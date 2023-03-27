"""
if 条件：
    满足条件1
    满足条件2
    满足条件3
    ...
else:
    满足条件4
    ...
"""

age = int(input('Please input your age:'))
if age >= 18:
    print('You are an adult')
    print('You need to cost $10')
else:
    print('You are a kid, play for free')

print('Have a nice time')
