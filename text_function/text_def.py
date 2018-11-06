"""
	用于测试函数定义 def
	在python中 一般采用传值调用，
	但当传入的参数为对象引用时，采用传址调用

	关于python的可变参数
	在定义函数时，参数列表中
	一个加*的参数表示从此处到参数结束，所有的参数全部被认为成一个元组（参数不可变）
	加**的则被认为时一个字典
	这时调用函数的方法则需要采用arg1 = value1, arg2 = value2这样的形式
	可变参数的例子见text_object/text_ploy.py

	author:Benjamin
"""


def print_hello():
	print("hello world")


def swap(a, b):
	return b, a


def max(a, b):
	if a > b:
		return a
	else:
		return b


def is_prime(num):
	for i in range(2, num//2):
		if num % i == 0:
			return 0
		else:
			return 1


print("###########################")#这里可以添加end=""来防止换行
print_hello()
print("swap({0}, {1}) = {2}".format(10, 20, swap(10, 20)))
print("max(100, 200) = " + str(max(100, 200)))
print("isPrime(13) = " + str(is_prime(13)))
