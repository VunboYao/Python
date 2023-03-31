"""
for 临时变量 in 待处理数据集(序列)：
    执行操作
else:
    循环正常执行完后（不是通过break跳出而中断的）
"""

for c in 'Vunbo':
    print(c)


print('-----------practice---------')

name = 'VunboYao is the best man'

number = 0
for c in name:
    if c == 'a':
        number += 1
else:
    print('All OK')

print(f'total: {number} a')
