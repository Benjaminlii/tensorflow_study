"""
    这个.py用于测试tf中的变量Variable
    打印一个增量

    op是指操作，也就是Session中执行的动作
    在tf中，首字母小写的都是op，首字母大写的是类，类中包含了op

    author:Benjamin
"""
import tensorflow as tf

# 定义变量v1,加法op new_variable存放自加1之后的新的v1,和更新v1的op update给v1赋值新的v1来更新v1
v1 = tf.Variable(0, name="variable1")
new_variable = tf.add(v1, 1)
update = tf.assign(v1, new_variable)

# 重点！！！凡是变量，都必须先进行初始化，下面的op用于初始化所有变量
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(v1))
    for _ in range(5):
        sess.run(update)
        print(sess.run(v1))
