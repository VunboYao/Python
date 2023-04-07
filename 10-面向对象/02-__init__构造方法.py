class Student:

    # 构造方法
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print(f'Student init')

    def speak(self):
        print(f'My name is {self.name}, my age is {self.age}, and my tel is {self.tel}')


emma = Student('Emma', 20, 166)
emma.speak()
