"""
创建一个自定义包，名称为:my_utils (我的工具)
在包内提供2个模块
• str_util.py (字符串相关工具，内含:)
    • 函数:str_reverse(s)，接受传入字符串，将字符串反转返回
    • 函数:substr(s, x, y)，按照下标x和y，对字符串进行切片
• file_util.py(文件处理相关工具，内含:)
    • 函数:print_file_info(file_name)，接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
    • 函数:append_to_file(file_name, data)，接收文件路径以及传入数据，将数据追 加写入到文件中
"""

# 字符串相关工具
# import my_utils.str_util
from my_utils import str_util as s

# foo = my_utils.str_util.str_reverse('Hello')
foo = s.str_reverse('Hello')
print(f'Hello反转后的字符串是：{foo}')

bar = s.substr('I love you!', 2, 6)
print(f'切片后的数据是：{bar}')

# 文件处理相关工具
from my_utils import file_util as f
import random
f.print_file_info('python.txt')
f.append_to_file('python.txt', f'Hello World => {random.randint(1, 10)}')
