# Tensorflow

## tf.shap 和 tf.get_shape().as_list()的区别

- tf.shape()返回的是一个tensor对象，需要使用sess.run()进行打印
- tf.get_shape()返回的是一个TensorShape对象，需要使用as_list()转换成列表，然后就和sess.run(tf.shape())的结果是一致的

## tf.identity()

```python
# 输出一个shape和content都与input一样的tensor
tf.identity(
	input,
	name=None
)
```
