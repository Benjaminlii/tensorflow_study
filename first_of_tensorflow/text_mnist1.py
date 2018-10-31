"""
    轮子
    author:Benjamin
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 载入mnist
mnist = input_data.read_data_sets("MNIST_DATA", one_hot=True)

# 批次大小
BATCH_SIZE = 50
BATCH_NUM = mnist.train.num_examples // BATCH_SIZE

# 变量x和y
x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

# 第一层神经网络
Weight = tf.Variable(tf.zeros([784, 10]))
biases = tf.Variable(tf.zeros([10]))
answer = tf.matmul(x, Weight) + biases

# 交叉熵损失函数和梯度下降训练法
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=answer))
train_set = tf.train.GradientDescentOptimizer(0.3).minimize(loss)

# 计算结果和精确率
consequence = tf.equal(tf.arg_max(y, 1), tf.arg_max(answer, 1))
precision = tf.reduce_mean(tf.cast(consequence, tf.float32))

# 会话
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    for i in range(20+1):
        for _ in range(BATCH_NUM):
            x_data, y_data = mnist.train.next_batch(BATCH_SIZE)
            sess.run(train_set, feed_dict={x: x_data, y: y_data})
        pre = sess.run(precision, feed_dict={x: mnist.train.images, y: mnist.train.labels})
        print("After %2d set(s), precision is %f" % (i, pre))


