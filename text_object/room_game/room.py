"""
尝试用python面向对象写一个之前Java写过的房间游戏
这是其中的Room类
author：Benjamin
"""


class Room:
    def __init__(self, name):
        # exits为出口，key为方向，value为key方向上的Room
        self.__exits = {}
        self.__name = name

    @property
    def get_name(self):
        # 返回当前Room的名字
        return self.__name

    def add_exit(self, exit1, room):
        # 为当前Room增加一个exit1方向上的Room
        self.__exits[exit1] = room

    def get_exit_room(self, exit1):
        # 得到当前Room在exit1方向上的Room
        return self.__exits[exit1]

    @property
    def get_direction(self):
        # 得到一个当前Room拥有的出口的列表
        s = ""
        for key in self.__exits:
            s += "{0} ".format(key)
        return s

# one = Room('2125')
# one.add_exit("east", "2126")
# one.add_exit("north", "2127")
# print(one.get_name())
# print(one.get_direction())
# print(one.get_exit_room("east"))
