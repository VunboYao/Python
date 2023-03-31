"""
局部变量：函数内的变量，外部无法使用
全局变量：全局的变量，函数内外均可使用

函数内使用全局变量：global 变量
"""

# 全局变量
num = 100


def test_a():
    print(f"test_a:", num)


def test_b():
    # 局部变量
    # num = 500
    global num
    num = 500
    print(f"test_b: {num}")


test_a()
test_b()
print(num)  # 如果使用global关键字后，此处变更为500
