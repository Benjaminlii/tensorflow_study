"""
    用于测试神经网络中的逆向传播

    传入体积和质量，算出y，y=1表示合格，y=0表示不合格

    不知道为什么，误差很大，有0.26之多
    然而30w次的训练只能减小0.000225
    还是说我对这个误差的理解有问题

    After 2999900 training step(s), loss on all data is 0.1072986126
    w1 =  [ [-0.11337509  0.16022703  0.09648883  0.16816367 -0.25676027  0.23957446]
            [-0.25880048  0.3657634   0.2202563   0.3838952  -0.5861608   0.5469052 ]]
    w2 =  [ [-0.20815966]
            [ 0.29419935]
            [ 0.17715739]
            [ 0.3087823 ]
            [-0.47144282]
            [ 0.43989706]]

    author:Benjamin
"""
import tensorflow as tf
import numpy as np

# BATCH_SIZE为每次输入的数据的数量
BATCH_SIZE = 8
# 数字为随机数种子
rng = np.random.RandomState(24516)

# X为32*2的矩阵，作为输入集
X = rng.rand(64, 2)
# 制作数据集的标签（正确答案）
Y = [[int(x1 + x2 > 1)] for (x1, x2) in X]
print("X = ", X)
print("Y = ", Y)

# 神经网络的正向传播
# 传入值
x  = tf.placeholder(tf.float32, shape=(None, 2))
# 标准答案
y_ = tf.placeholder(tf.float32, shape=(None, 1))

w1 = tf.Variable(tf.random_normal([2, 6]))
w2 = tf.Variable(tf.random_normal([6, 1]))

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 损失函数及逆向传播方法
loss = tf.reduce_mean(tf.square(y-y_))

# 指数下降学习率
global_step = tf.Variable(0, trainable=False)
learn_rate = tf.train.exponential_decay(0.1, global_step, 4, 0.99, staircase=True)
train_step = tf.train.GradientDescentOptimizer(learn_rate).minimize(loss)

# 会话
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    # 输出未训练的参数
    print("w1 = ", sess.run(w1))
    print("w2 = ", sess.run(w2))
    print("\n")

    # 进行重复的训练
    STEPS = 3000000
    for i in range(STEPS):
        start = (i * BATCH_SIZE) % 64
        end = start + BATCH_SIZE
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})
        if i % 100 == 0:
            total_loss = sess.run(loss, feed_dict={x: X, y_: Y})
            print("After %d training step(s), loss on all data is %.10f" % (i, total_loss))

    # 输出训练后的参数
    print("\n")
    print("w1 = ", sess.run(w1))
    print("w2 = ", sess.run(w2))
