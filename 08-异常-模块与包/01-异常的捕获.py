"""
try:
    可能发生错误的代码
except [异常 as 别名]:
    出现异常时执行的代码
[else:]
    未出现异常时应做的事情
[finally:]
    此处获取的变量，try和except中只能获取一个，如果try中报错，则只能获取except中的变量
    需要注意此处变量获取的方式
    不管是否出现异常都会执行的事情

注意事项：
    - 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获所有异常
    - python中，变量作用域由函数、类、模块或代码块确定，try...expect中不会创建新的作用域

如何捕获所有异常：
    - except:
    - except Exception:
"""

# try:
#     f = open('python.txt', 'r')
#     # print(Name)
#     # 1 / 0
# # 捕获多个异常时，可以把要捕获的异常类型的名字，放到 except 后，并使用元组的方式进行书写
# except (NameError, ZeroDivisionError, FileNotFoundError) as e:
#     print(f'此处发生了错误: \n {e}')
#     f = open('python.txt', 'w')


# 捕获所有异常
# try:
#     print(Name)
# except Exception as e:
#     print(f'捕获所有的异常, {e}')

# 异常 else
# try:
#     print(1)
# except Exception as e:
#     print(e)
# else:
#     print('else, 没有异常的时候执行的代码')

# 异常的finally
try:
    f = open('python.txt', 'r')
except Exception as e:
    f = open('python.txt', 'w')
    print(f'catch Error:{e}')
else:
    print('没有错误')
finally:
    f.close()
    print(f'不管是否有错误，都会执行')

# 更优的写法
# try:
#     with open('python.txt', 'r') as f:
#         print(f)
# except FileNotFoundError as e:
#     with open('python.txt', 'w') as f:
#         print(f)
# finally:
#     print('最后都执行了finally')
