"""
    用于计算y = ax2 + bx + c 的神经网络

    本例的方程为 y = 2.4x2 + 1.5x + 0.9

    author:Benjamin
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 创建x_data和y_data,使用numpy生成随机点，并且生成噪声noise
x_data = np.linspace(-0.5, 0.5, 200, dtype=np.float32)[:, np.newaxis]
noise = np.random.normal(0, 0.03, x_data.shape).astype(np.float32)
# 特征缩放
y_data = (2.4 * np.square(x_data) + 1.5 * x_data + 0.9 + noise)/18

# 传入和传出的数据
x = tf.placeholder(np.float32, [None, 1])
y = tf.placeholder(np.float32, [None, 1])

# 制作神经网络隐藏层 神经元为10个
Weight_L1 = tf.Variable(tf.random_normal([1, 10]))
biases_L1 = tf.Variable(np.zeros([1, 10]).astype(np.float32))
Wx_plus_b_L1 = tf.matmul(x, Weight_L1) + biases_L1

L1 = tf.nn.tanh(Wx_plus_b_L1)

# 制作神经网络输出层
Weight_L2 = tf.Variable(tf.random_normal([10, 1]))
biases_L2 = tf.Variable(np.zeros([1, 1]).astype(np.float32))
Wx_plus_b_L2 = tf.matmul(L1, Weight_L2) + biases_L2
answer = tf.nn.relu(Wx_plus_b_L2)

# 代价函数和梯度下降法训练
loss = tf.reduce_mean(tf.square(y - answer))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 会话
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    for i in range(20001):
        sess.run(train_step, feed_dict={x: x_data, y: y_data})
        if i % 1000 == 0:
            print("After %4d steps, loss is %1.10f" % (i, sess.run(loss, feed_dict={x: x_data, y: y_data})))
    plt.figure()
    plt.scatter(x_data, y_data)
    plt.plot(x_data, sess.run(answer, feed_dict={x: x_data, y: y_data}), "r-", lw=5)
    plt.show()
