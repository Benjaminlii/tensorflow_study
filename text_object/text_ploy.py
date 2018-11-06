"""
    用于测试python中的多态

    在各种面向对象的程序设计语言中，多态的概念都大致相同
    在此不多做赘述

    python多态实现的条件为方法重写和继承
    与Java不同，python为弱类型语言，不讲究对象的类型和对象变量的类型
    所以没有父类对象变量引用子类对象这一项

    关于python的可变参数
    在定义函数时，参数列表中
    一个加*的参数表示从此处到参数结束，所有的参数全部被认为成一个元组（参数不可变）
    加**的则被认为时一个字典
    这时调用函数的方法则需要采用arg1 = value1, arg2 = value2这样的形式

    author:Benjamin
"""


class People:
    def eat(self):
        print("人都会吃饭")


class Chinese(People):
    def eat(self):
        print("中国人用筷子吃饭")


class English(People):
    def eat(self):
        print("英国人用刀叉吃饭")


class Indian(People):
    def eat(self):
        print("印度人用手吃饭")


def everybody_eat(*people_list):
    for i in people_list:
        if isinstance(i, People):
            i.eat()
        else:
            print("error!")


everybody_eat(People(), Chinese(), English(), Indian())
