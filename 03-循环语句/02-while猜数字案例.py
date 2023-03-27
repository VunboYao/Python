import random
num = random.randint(1, 100)

times = 0
while True:
    times += 1
    guess_number = int(input('Please input your guess number:'))

    if guess_number > num:
        print('should be more smaller')
    elif guess_number < num:
        print('should be more bigger')
    else:
        print(f'Congratulation You use {times} times get the number: {num}')
        break  # 将True存储到一个变量中，最后将变量置为False，替换break
