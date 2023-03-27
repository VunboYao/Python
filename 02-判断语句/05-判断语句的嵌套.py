"""
if 条件1：
    满足条件1
    满足条件1

    if 条件2：
        满足条件2
        满足条件2

"""
print('Welcome to our zoo')
if int(input('Please input your age:')) >= 18:
    print('You are an adult')
    print('If your VIP > 3, free')

    if int(input('Please your VIP:')) > 3:
        print('Congratulation, free')
    else:
        print('Sorry, you need to cost $10')
else:
    print('Welcome kid')
