"""
    这个.py用于测试tf中的常量constant
    计算矩阵的乘法
    由于是我编写的第一个使用TensorFlow框架的DL程序
    (其实根本算不上)
    所以内容都来自网课
    在这里Mark一下网课的链接：https://www.bilibili.com/video/av20542427/?p=4

    为什么会输出GPU的信息呢？？？查也查不到

    author:Benjamin
"""
import tensorflow as tf

w1 = tf.constant([])
w2 = tf.constant([])
a = tf.matmul(w1, w2)


# 定义出tf中默认的会话Session，并启动默认的图
with tf.Session() as sess:
    # 调用Session的run方法开始计算
    result = sess.run(a)
    print(result)
