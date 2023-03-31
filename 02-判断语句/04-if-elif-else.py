"""
判断条件是互斥有序的

if 条件：
    满足条件1
    满足条件2
    满足条件3
    ...
elif:
    # elif 可以有多个
    满足条件4
    ...
else:
    满足条件5
    ...
"""

age = int(input('Please input your age:'))

if 18 <= age < 45:
    print('You are an adult')
    print('You need to cost $10')
elif age >= 45:
    print('Your are an old people')
    print('You need to cost $5')
else:
    print('You are a kid, play for free')

print('Have a nice time')

print('----------practice--------')

number = 10

if int(input('Please input my guess number 1-10:')) == number:
    print('Congratulation Good')
elif int(input('Sorry, please again:')) == number:
    print('Congratulation Nice')
elif int(input('Sorry, once again:')) == number:
    print('Congratulation Perfect')
else:
    print('Sorry, all failed, it\'s', number)
