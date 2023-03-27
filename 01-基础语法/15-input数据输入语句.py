"""
input获取的输入数据都是字符串类型
    如果需要将字符串转换成数字类型, 需要用到int(变量)
"""
name = input('Please tell me, who are you?:')
print('Robot:', name)

num = input('Please input your card:')
num = int(num)
print(type(num), num)

user_name = input('Input your name:')
user_type = input('Input your VIPLevel:')
print(f'Hello, {user_name}, yor are the best VIP: {user_type}, Welcome!')
