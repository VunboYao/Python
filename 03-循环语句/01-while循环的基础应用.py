"""
while 条件：
    条件满足，做的事情1
    条件满足，做的事情2
    条件满足，做的事情3
    ...

补充
    条件应该是True
"""

num = 1
total = 0

while num <= 100:
    total += num
    num += 1

print(f'Done, the total is {total}')

