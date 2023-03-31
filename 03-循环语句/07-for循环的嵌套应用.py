"""
for 临时变量 in 序列：
    do something
    ...
    for 临时变量 in 序列：
        do something
        ...
"""
# 预先定义变量
i = 0

for i in range(100):
    for j in range(10):
        print(f'今天是第{i + 1}天，送的第{j + 1}朵花')

# 循环内的临时变量，实际可以访问到，但是不建议这么做
# 如果实在需要在循环外访问循环内的临时变量，可以在循环外预先定义
print(i)
