"""
    初试卷积神经网络（cnn）
    author:Benjamin
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_DATA", one_hot=True)

BITCH_SIZE = 50
BITCH_NUM = mnist.train.num_examples // BITCH_SIZE

# 函数定义------------------------------------------------


def weight_variable(shape):
    # 得到服从正态分布的变量weight，标准差为0.1
    return tf.Variable(tf.truncated_normal(shape, stddev=0.1))


def biases_variable(shape):
    # 得到值全为0.1的biases;
    return tf.Variable(tf.constant(0.1, shape=shape))


def conv2d(x, W):
    # 卷积操作，strides为卷积步长，前后两个1为固定，中间两个数值分别为行步长和列步长
    # padding为是否用0填充边缘，SAME为填充，VALID为不填充
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    # 池化操作，ksize为池化的尺寸2x2，stride为池化的步长2x2，padding同上
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


# 输入输出结构--------------------------------------------


x_ = tf.placeholder(tf.float32, [None, 28*28])
x = tf.reshape(x_, [-1, 28, 28, 1])
y = tf.placeholder(tf.float32, [None, 10])
prob = tf.placeholder(tf.float32)  # 使用drop的参数


# 搭建网络-----------------------------------------------

# 第一层卷积
weight_con1 = weight_variable([5, 5, 1, 32])  # 第一个卷积层卷积核为5x5，有32个
biases_con1 = biases_variable([32])  # 每个卷积核有一个偏置值
one_con1 = tf.nn.relu(conv2d(x, weight_con1) + biases_con1)
answer_con1 = max_pool_2x2(one_con1)

# 第二层卷积
# 此时经过第一层卷积，answer的尺寸为28/2x28/2x32 = 14x14x32
weight_con2 = weight_variable([5, 5, 32, 64])
biases_con2 = biases_variable([64])
one_con2 = tf.nn.relu(conv2d(answer_con1, weight_con2) + biases_con2)
answer_con2 = max_pool_2x2(one_con2)

# 全连接---------
# 此时answer的尺寸为14/2x14/2x64 = 7x7x64
weight_fc1_ = weight_variable([7*7*64, 1024])

# dropout操作
keep_prob = tf.placeholder(tf.float32)
weight_fc1 = tf.nn.dropout(weight_fc1_, keep_prob)

biases_fc1 = biases_variable([1024])
x_fc1 = tf.reshape(answer_con2, [-1, 7*7*64])
answer_fc1 = tf.nn.relu(tf.matmul(x_fc1, weight_fc1) + biases_fc1)
# --------------

# 输出层
weight_fc2_ = weight_variable([1024, 10])
weight_fc2 = tf.nn.dropout(weight_fc2_, keep_prob)
biases_fc2 = biases_variable([10])
answer_fc2 = tf.nn.softmax(tf.matmul(answer_fc1, weight_fc2) + biases_fc2)

# 代价函数和训练-----------------------------------------
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=answer_fc2))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 结果和精确率
answer = tf.equal(tf.arg_max(answer_fc2, 1), tf.arg_max(y, 1))
precision = tf.reduce_mean(tf.cast(answer, tf.float32))

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    for i in range(20+1):
        for j in range(BITCH_NUM):
            x_data, y_data = mnist.train.next_batch(BITCH_SIZE)
            sess.run(train_step, feed_dict={x_: x_data, y: y_data, keep_prob: 0.5})
            if(j % 100 == 0):
                pre = sess.run(precision, feed_dict={x_: x_data, y: y_data, keep_prob: 0.5})
                print("After %3d step(s), precision is %f" % (j, pre))
