"""
什么是模块：
    - 一个 Python 文件，以.py结尾，则是模块
    - 可以定义函数、类和变量，模块中可以执行代码

模块的导入方式
    - [from 模块名] import [模块名｜类｜变量｜函数｜*] [as 别名]
    - import 模块名
    - from 模块名 import 类、变量，方法等
    - from 模块名 import *
    - import 模块名 as 别名
    - from 模块名 import 功能名 as 别名
"""

# import 模块名
# import time
#
# print('Start')
# time.sleep(3)
# print('End')

# from 模块名 import 方法
# from time import sleep
# print('start')
# sleep(3)
# print('end')

# from 模块名 import *
# from time import *
# print('start')
# sleep(3)
# print('end')

# as 定义别名
import time as t
print('start')
t.sleep(3)
print('end')
