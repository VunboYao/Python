"""
bool类型：首字母大写
    True 本质是：1
    False 本质是：0
    变量名称 = 布尔类型字面量

也可以通过比较运算符得到bool类型
    ==
    !=
    >
    <
    >=
    <=
"""

bool_true = True
print(type(bool_true), bool_true)

bool_1 = 5 > 3
print(f"bool_1的类型是:{bool_1}")

bool_2 = 23 < 12
print(f"bool_2的类型是:{bool_2}")  # False

# 浮点数的比较
print(f"12.0 == 12吗？{12.0 == 12}")  # True
