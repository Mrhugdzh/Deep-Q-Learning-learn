from random import sample
import tensorflow as tf

def sample_nosiy(shape):
    """
        描述：产生正态分布随机数据

        输入：shape：需要的数据维度信息

        返回：noise：产生的正态分布数据
    """
    noise = tf.random_normal(shape)
    return noise

def noisy_dense(x, size, name, bise=True,actionve_fn=tf.identity):
    """
        描述：使用Noisy Net网络

        输入：x：输入数据；size：输出尺寸，bise：是否有偏置参数，activate_fn：激活函数

        输出：经过该层网络传播的输出
    """
    # ! f(x)的公式内容，用于生成w和b的随机噪声，减少参数数量
    def f(x):
        return tf.multiply(tf.sign(x), tf.pow(tf.abs(x), 0.5))

    # ! w 和 b来自的正太分布
    mu_init = tf.random_uniform_initializer(minval=-1*1/tf.pow(x.get_shape().as_list()[1], 0.5),
                                            maxval=1*1/tf.pow(x.get_shape().as_list()[1], 0.5))
    sigma_init = tf.constant_initializer(0.4*1/tf.pow(x.get_shape().as_list()[1], 0.5))
    p = sample_nosiy([x.get_shape().as_list()[1], 1])
    q = sample([1,size])
    f_p=f(p)
    f_q=f(q)

    # ! 接下计算w和b的噪声
    w_eplison = f_q*f_p
    b_eplison=tf.squeeze(f_q)

    # ! 生成另外的参数
    w_mu=tf.get_variable(name='w_mu',shape=[x.get_shape().as_list()[1], size], initializer=mu_init)
    w_sigma=tf.get_variable(name='w_sigma', shape=[x.get_shape().as_list()[1],size], initializer=sigma_init)
    w = w_mu + tf.multiply(w_sigma, w_eplison)

    if bise:
        b_mu=tf.get_variable(name='b_mu',shape=[size], initializer=mu_init)
        b_sigma=tf.get_variable(name='b_sigma',shape=[size],initializer=sigma_init)
        b=b_mu+tf.multiply(b_sigma,b_eplison)
        y=tf.multiply(x, w) + b
        return actionve_fn(y)
    else:
        return actionve_fn(tf.multiply(x,w))