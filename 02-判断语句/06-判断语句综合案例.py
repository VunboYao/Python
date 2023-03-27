"""
1.数字随机产生，范围1-10
2.有3次机会猜测数字，通过3层嵌套判断实现
3.每次猜不中，会提示大了/小了
"""

'''
import random

num = random.randint(1, 10)
if num > 5:
    print('number should be more bigger')

    if num > 8:
        print('number should be more bigger')

        if num > 9:
            print('number is 10')
        else:
            print('number is 9')
    else:
        print('number should be more smaller')

        if num > 7:
            print('number is 8')
        else:
            if num > 6:
                print('number is 7')
            else:
                print('number is 6')
else:
    print('number should be more smaller')

    if num > 3:
        print('number should be more bigger')

        if num > 4:
            print('number is 5')
        else:
            print('number is 4')
    else:
        print('number should be more smaller')

        if num > 2:
            print('number is 3')
        else:
            if num > 1:
                print('number is 2')
            else:
                print('number is 1')

print(f"number => {num}")
'''

import random

num = random.randint(1, 10)
guess_num = int(input('please input your digital:'))

if guess_num == num:
    print('Congratulation You are right 1')
else:
    if guess_num > num:
        print('Should be more smaller')
    else:
        print('Should be more bigger')

    guess_num = int(input('please input your digital:'))

    if guess_num == num:
        print('Congratulation You are right 2')
    else:
        if guess_num > num:
            print('should be more smaller')
        else:
            print('should be more bigger')

        guess_num = int(input('please input your digital:'))

        if guess_num == num:
            print('Congratulation you are right 3')
        else:
            print('Sorry, you are failed')

print(f'The num is {num}')
