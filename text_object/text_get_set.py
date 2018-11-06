"""
    用于测试set和get函数
    @property 和 @xxx.setter

    @property   用于把函数装饰成成员属性
    @xxx.setter 用于把函数装饰成成员属性的同时加入更改成员变量的功能
    注：只有在定义了@property之后，才可以定义一个成员变量的@xxx.setter函数

    上述操作主要用于将setter()和getter()的调用直接转化成对象属性的调用
    简化代码，同时保证私有属性的封装不被破坏

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
        return "Person: [name = {0}, age = {1}]".format(self.name, self.age)


p = Person("张兆伟", 19)
# print(p.name)
# print(p.age)
print(p)
p.age = 20
print(p)
