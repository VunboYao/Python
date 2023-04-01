"""
- 包就是一个文件夹，包含了一个__init__.py文件，该文件可用于包含多个模块文件，从逻辑上看，包的本质依然是模块
- __init__.py中控制着包的导入行为
"""

# 导入1
# import my_package.foo_module
# import my_package.bar_module
#
# my_package.foo_module.foo()
# my_package.bar_module.bar()

# 导入2
from my_package import foo_module
from my_package import bar_module
foo_module.foo()
bar_module.bar()
