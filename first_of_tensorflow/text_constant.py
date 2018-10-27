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

x = tf.constant([[0.53693543, 0.05866297]])
w1 = tf.constant([ [-0.11337509, 0.16022703, 0.09648883, 0.16816367, -0.25676027, 0.23957446],
                   [-0.25880048, 0.3657634,  0.2202563,  0.3838952, -0.5861608,  0.5469052 ]])
w2 = tf.constant([ [-0.20815966],
                   [ 0.29419935],
                   [ 0.17715739],
                   [ 0.3087823 ],
                   [-0.47144282],
                   [ 0.43989706]])
a = tf.matmul(x, w1)
y_ = tf.matmul(a, w2)
y = int(0.53693543+0.05866297<1)

# 定义出tf中默认的会话Session，并启动默认的图
with tf.Session() as sess:
    # 调用Session的run方法开始计算
    result = sess.run(y_)
    print(result, "\n", y)
