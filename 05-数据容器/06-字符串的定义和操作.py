"""
索引：
    - 从前向后，从0开始
    - 从后向前，从-1开始
    - 无法修改

常用方法：
    - index = str.index('xxx')
    - new_str = str.replace('a', 'b')
    - new_list = str.split(分割符)
    - new_str = str.strip()
    - new_int = str.count(字符串)
    - len
"""

# 通过下标获取值
my_str = 'VunboYaoYao'
print(f'获取Y:{my_str[-3]}')

# 不可根据下标修改值
# my_str[0] = 'v'
# print(my_str)

# index方法
y_index = my_str.index('Y')
print(f'Y的索引是：{y_index}')

# replace，num1 => num2 全部替换操作。 返回一个新的字符串
new_str = my_str.replace('Y', 'B')
print(f'str.replace("Y", "B")新的字符串是{new_str}')

# split，返回一个新的列表
my_str = 'Hello World I like Python'
new_list = my_str.split(' ')  # 空格
print(f'split操作返回的列表是{new_list}')

# strip() 去除前后的空格; strip(字符串)，去除前后指定的字符串
my_str = '  Hello World I like Python   '
new_str = my_str.strip()
print(f'移除空格，新的字符串是:{new_str}')

my_str = '10Hello World I like Python 01'
new_str = my_str.strip('10')  # 指定前后的字符串1和0
print(f'移除前后的10，新的字符串是:{new_str}')

# count(字符串)
count = my_str.count('10')
print(f'10出现的次数是：{count}')

# len获取长度方法
length = len(my_str)
print(f'长度是{length}')


print('---------practice---------')
test_str = 'itheima itcast boxuegu'
count = test_str.count('it')
new_str = test_str.replace(' ', '|')
list_str = new_str.split('|')
print(f'{count}个it字符')
print(f'替换空格后：{new_str}')
print(f'按照|拆分后：{list_str}')

