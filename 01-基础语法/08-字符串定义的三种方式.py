"""
1.单引号
2.双引号
3.三引号（如果有变量接收，则是多行字符串，否则，就是多行注释）
4.转义字符\
"""

name = 'VunboYao'
print(type(name))

double_quote = "VunboYao"
print(type(double_quote))

triple_quote = """
Vunbo
Yao
"""
print(type(triple_quote), triple_quote)
