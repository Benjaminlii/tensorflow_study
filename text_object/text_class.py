"""
    用于测试建立第一个python类

    python中成员变量位于初始化函数中
    可以在后续继续添加，但新的成员变量不属于类

    python的方法不具有重载

    author：Benjamin
"""


class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def __str__(self):
        return "Student:[name = "+str(self.name)\
               +", age = "+str(self.age)\
               +", student_id= "+str(self.student_id)+"]"


stu1 = Student("Benjamin", 19, "04173130")
print(stu1)
