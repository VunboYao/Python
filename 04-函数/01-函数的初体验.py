name = 'VunboYao'
name2 = 'Emma'
length = len(name)
print(length)

print('---------自定义len-----------')


# for遍历自定义实现len
def my_len(data):
    count = 0
    for i in data:
        count += 1
    return count


print(f'自定义的函数的length:', my_len(name2))
