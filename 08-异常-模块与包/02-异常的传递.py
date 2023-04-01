"""
- 异常具有传递性，只需要在外层函数中设置异常捕获，最终所有的异常都会被捕获
"""


def func01():
    print('This is func01 start')
    num = 1 / 0
    print('This is func01 end')


def func02():
    print('This is func02 start')
    func01()
    print('This is func02 end')


def main():
    try:
        func02()
    except Exception as e:
        print(f'catch Error: {e}')

main()

