"""
for 临时变量 in 序列：
    do something
    ...
    for 临时变量 in 序列：
        do something
        ...
"""

for i in range(100):
    for j in range(10):
        print(f'今天是第{i + 1}天，送的第{j + 1}朵花')
        