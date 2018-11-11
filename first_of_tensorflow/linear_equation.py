"""
    用于通过机器学习计算出y=kx+b的k和b

    本例中 y = 2.5x + 3.7

    author:Benjamin
"""
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# 定义传入的数据，用numpy生成300个随机数
x_data = np.random.rand(300)
noise = np.random.normal(0, 0.03, x_data.shape).astype(np.float32)
y_data = (x_data * 2.5 + 3.7) + noise
k = tf.Variable(0.0)
b = tf.Variable(1.0)

x = tf.placeholder(tf.float32)
y_ = tf.placeholder(tf.float32)

y = k * x + b

# 代价函数和优化器
loss = tf.reduce_mean(tf.square(y-y_))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

# 会话
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    for i in range(10000):
        sess.run(train_step, feed_dict={x: x_data, y_: y_data})
        if i % 1000 == 0:
            print("After %5d training steps, k is %f, b is %f." % (i, sess.run(k), sess.run(b)))
    print("Final k is %f, b is %f." % (sess.run(k), sess.run(b)))
    plt.figure()
    plt.scatter(x_data, y_data)
    plt.plot(x_data, sess.run(y, feed_dict={x: x_data}), "r-", lw=0.5)
    plt.show()
