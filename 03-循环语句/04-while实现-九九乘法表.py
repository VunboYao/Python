"""
print(xx, end=""): 打印的末尾不换行
\t 实现多行字符串对齐
"""

i = 1
while i <= 9:
    msg = ''
    j = 1
    while j <= i:
        msg += f'{j} * {i} = {i * j}\t'
        j += 1
    print(msg)
    i += 1

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f'{j} * {i} = {i * j}\t', end="")
#         j += 1
#     i += 1
#     print()
