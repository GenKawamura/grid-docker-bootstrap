# -*- coding: utf-8 -*-

import input_data
import tensorflow as tf

# Downloading MNIST data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Setting Weights and Threasholds (Initial values are 0)
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Feature vectors during training
x = tf.placeholder("float", [None, 784])

# Softmax function
y = tf.nn.softmax(tf.matmul(x, W) + b)

# True labels are set
y_ = tf.placeholder("float", [None,10])

# Loss function is defined by cross entropy
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

# Define lerning methods (Stepsize 0.01 and descrite methods to reach minimum cross entropy)
train_step = tf.train.GradientDescentOptimizer(0.005).minimize(cross_entropy)

# Prepare session
sess = tf.Session()

# Initialize valiables
init = tf.initialize_all_variables()
sess.run(init)

for i in range(1000):
    # Data for mini batch
    batch_xs, batch_ys = mnist.train.next_batch(100)
    # Update data according to descrete
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# Define a function to return correct prediction
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

# See results
print sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
