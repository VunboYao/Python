"""
字符串格式化语法
    "%占位符" % 变量

常用地占位符
    字符串： %s
    整数：   %d
    浮点数：  %f

辅助符号"m.n"控制数据的宽度和精度
    m，控制宽度，要求是数字（很少使用），设置的宽度小于数字自身，不生效
    .n，控制小数点精度，要求是数字，会进行小数的四舍五入

示例：
    %5d: 控制5位展示，如11，[空格][空格][空格]11，用三个空格补足
    %5.2f: 控制宽度为5位，小数点精度设置为2。 小数点和小数部分也算入宽度。
        如11.345设置了%7.2f之后，结果是[空格][空格]11.35
    %.2f：不限制宽度，只设置了小数点精度为2。
        如11.345设置了%.2f之后，结果是11.35
"""

first_name = 'Vunbo'
last_name = 'Yao'
number = 666

# 占位的形式：%s
message = "My fullname is %s%s, and my score is %s" % (first_name, last_name, number)
print(message)

name = 'Vunbo'
age = 20
number = 20.99
message = "name: %s, age: %d, score: %f" % (name, age, number)
print(message)

print('------精度控制------')
num1 = 11
num2 = 11.345
print('数字11宽度限制5，结果是: %5d' % num1)
print('数字11宽度限制1，结果是: %1d' % num1)  # 小于宽度，不变
print('数字11.345宽度限制7，小数精度2，结果是: %7.2f' % num2)  # 补2个空格
print('数字11.345宽度不限制，小数精度2，结果是: %.2f' % num2)
