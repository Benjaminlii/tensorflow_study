"""
    MNIST数据集分类的简单版本

    @author:Benjamin
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 载入数据集
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

# 批次大小及个数
BATCH_SIZE = 50
N_BATCH = mnist.train.num_examples // BATCH_SIZE

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

# 神经网络
Weight = tf.Variable(tf.ones([784, 10]))
biases = tf.Variable(tf.zeros([10]))
answer = tf.nn.softmax(tf.matmul(x, Weight) + biases)

# 均方误差损失函数，交叉熵损失函数和梯度下降法
# 均方误差通常用于回归问题，交叉熵用于分类问题
# loss = tf.reduce_mean(tf.square(answer - y))
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=answer))
train_step = tf.train.GradientDescentOptimizer(0.3).minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()

# 计算结果和准确率，结果为True和false构成的一维张量，准确率即对结果转换为浮点再求平均值
consequence = tf.equal(tf.argmax(y, 1), tf.argmax(answer, 1))
precision = tf.reduce_mean(tf.cast(consequence, tf.float32))

# 会话
with tf.Session() as sess:
    sess.run(init)
    for _ in range(20+1):
        for batch in range(N_BATCH):
            x_s, y_s = mnist.train.next_batch(BATCH_SIZE)
            sess.run(train_step, feed_dict={x: x_s, y: y_s})
        pre = sess.run(precision, feed_dict={x: mnist.test.images, y: mnist.test.labels})
        print("After %2d step(s), the precision is %f" % (_, pre))
