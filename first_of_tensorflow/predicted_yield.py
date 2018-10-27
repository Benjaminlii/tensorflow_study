"""
    预测产量
    author:Benjamin
"""
import tensorflow as tf
import numpy as np
BATCH_SIZE = 8
SEED = 23455

# 利润和成本
PROFIT = 1
COST = 9

# 拟造数据集
rng = np.random.RandomState(SEED)
X = rng.rand(32, 2)
Y_ = [[x1 + x2 + (rng.rand()/10-0.05)]for(x1, x2) in X]

# 定义正向传播过程
x = tf.placeholder(tf.float32, shape=(None, 2))
y_ = tf.placeholder(tf.float32, shape=(None, 1))
w1 = tf.Variable(tf.random_normal([2,1], stddev=1, seed=1))
y = tf.matmul(x, w1)

# 定义反向传播过程和损失函数
loss = tf.reduce_sum(tf.where(tf.greater(y, y_),COST*(y-y_),PROFIT*(y_-y)))
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)

# 生产会话
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    STEPS = 20000
    for i in range(STEPS):
        start = (i * BATCH_SIZE) % 32
        end = start + BATCH_SIZE
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y_[start:end]})
        if i % 500 == 0:
            print("After %d training steps, w1 is" % i, sess.run(w1))
    print("Final w1 is", sess.run(w1))
