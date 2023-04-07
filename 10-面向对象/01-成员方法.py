"""
1.类的组成
    - 类的属性，称之为：成员变量
    - 类的行为，称之为：成员方法

2.类和成员方法的定义语法
class 类名称：
    成员变量

    def 成员方法(self, 参数列表):
        方法体

对象 = 类名称()

3.self的作用
    - 表示类对象本身的意思
    - 只有通过self，成员方法才能访问类的成员变量
    - self出现在形参列表中，但是不占用参数位置，无需理会
"""


class Clock:
    id = None
    price = None

    def ring(self):
        print(f'do thing {self.id}, {self.price}')


clock1 = Clock()
clock1.id = '001'
clock1.price = '19.0'
clock1.ring()
