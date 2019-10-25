import tensorflow as tf
with tf.Session() as sess:
    x = tf.placeholder(tf.int32, name = "Input")
    out = tf.abs(x, name = "Output")

    tf.saved_model.simple_save(sess, "abs", inputs={"input": x}, outputs={"abs": out})
