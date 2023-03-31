""""
新序列 = 序列[起始下标:结束下标:步长]
"""

# 下标1开始，下标4(不含)结束，步长1
my_list = [1, 2, 3, 4, 5]
new_list = my_list[1:4]
print(f'截取从下标1开始，到4(不含)结束：{new_list}')

# 从头开始，到最后结束，步长1
my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[:]
print(f'从头开始，到最后结束，步长1:{new_tuple}')

# 从头开始，到最后结束，步长2
my_list = [1, 2, 3, 4, 5]
new_list = my_list[::2]
print(f'从头开始，到最后结束，步长2:{new_list}')

# 从头开始，到下标4(不含)结束，步长2
my_str = '12345'
new_str = my_str[:4:2]
print(f'从头开始，到下标4(不含)结束，12345步长2的字符串:{new_str}')

# 从头(最后)开始，到尾结束，步长-1(倒序)
my_str = '12345'
new_str = my_str[::-1]
print(f'12345从头(最后)开始，到尾结束，步长-1(倒序): {new_str}')

#
my_list = [1, 2, 3, 4, 5]
new_list = my_list[3:1:-1]
print(f'从下标3开始，到下标1(不含)结束，步长-1(倒序): {new_list}')

# 从头(最后)开始，到下标1(不含)结束，步长-2(倒序)
my_list = (1, 2, 3, 4, 5)
new_list = my_list[:1:-2]
print(f'从头(最后)开始，到下标1(不含)结束，步长-2(倒序): {new_list}')
