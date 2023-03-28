"""
continue（临时中断）：当前循环中断语句
break（永久中断）: 跳出当前循环语句
"""

for i in range(1, 6):
    print(f'continue: statement{i}')
    continue
    print('???')

for i in range(1, 11):
    print(f'break: statement{i}')
    if i > 5:
        break

for i in range(1, 5):
    print(f'外层的循环{i}')
    for j in range(1, 10):
        # 只会打印一次
        print(f'内层的循环{j}')
        break
