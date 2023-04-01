"""
- if __main__ == “__main__”表示，只有当程序是直接执行的才会进入if 内部，如果是被导入的，则if无法进入
- 当导入多个模块的功能时，且模块内有同名功能，当调用这个同名功能的时候，后面导入的会覆盖之前的
- __all__变量可以控制import *的时候哪些功能可以被导入
"""

import my_module
import her_module

from my_module import add
from her_module import add

from my_module import *

# my_module.add(1, 3)
add(4, 2)

# 错误，由于 my_module 中 __all__中未声明sub方法
# sub(5, 3)
