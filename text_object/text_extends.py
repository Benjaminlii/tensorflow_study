"""
    用于测试类的继承和方法的重写

    python可以实现多继承，不过不建议使用
    多继承格式：class A(B, C):   #A类同时继承B类和C类

    __str__()方法相当于Java中的toString()方法
    继承自object类
    一样可以被对象名直接调用

    子类的初始化函数可以调用父类的初始化函数来初始化父类那部分的成员变量
    格式为：父类名.__init__(self,[参数1，参数2.....])
    且应该出现在子类初始化函数的第一行

    类名.mro()可以得到相关类的继承层次结构
    dir(对象名)可以得到对象内属性的列表

    author:Benjamin
"""


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("error!")

    def __str__(self):
        return "Person: [name = {0}, age = {1}]"\
                .format(self.name, self.age)


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if 0 < score < 120:
            self.__score = score
        else:
            print("error!")

    def __str__(self):
        return "Student:[name = {0}, age = {1}, score = {2}]"\
                .format(self.name, self.age, self.score)


s = Student("张兆伟", 19, 80)
print(s)
s.age = 20
print(s)
