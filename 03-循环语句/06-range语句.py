"""
range(num)：获取一个从0开始，到num结束的数字序列（不含num本身）
range(num1, num2): 获取一个从num1到num2结束的数字序列（不含num2本身）
range(num1, num2, step):获取一个从num1到num2结束的数字序列（不含num2本身）,数字之间的步长，以 step 为准（默认为1）
"""

for i in range(10):
    print(f'{i}\t', end='')

print()

for i in range(5, 10):
    print(f'{i}\t', end='')
print()


for i in range(5, 10, 2):
    print(f'{i}\t', end='')
print()

print('----------practice-----------')
count = 0
for i in range(1, 100):
    if i % 2 == 0:
        count += 1
print(f'出现了{count}次偶数')
