r = open('word.txt', 'r', encoding='utf-8')

# read方式读取后返回的是一个字符串
# count = r.read().count('itheima')
# print(f'通过read()方法读取的字符串，获取其count: {count}')

count = 0
for line in r:
    # 去除\n换行符，并空格分割为list
    l_list = line.strip().split(' ')
    # 通过list.count获取数量
    count += l_list.count('itheima')

print(f'for循环获取itheima出现的次数：{count}')

r.close()