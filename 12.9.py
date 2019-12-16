from numpy import arange
from numpy import array
import numpy as np

m = array([arange(2), arange(2)])
print(m.shape)
n = array([[arange(3), arange(3)], [arange(3), arange(3)]])
print(n.shape)

# 多维数组的切片
# reshape改变维度

b = arange(24).reshape(2, 3, 4)
print(b)
print(b[:, 0, 0])
print(b[..., 0])  # 多个冒号可以用省略号代替
print(b[..., 0][0, :])  # 多次索引只要有效就可以
print(b[0, 1, :])
print(b[0, 1, ::2])  # 间隔选定元素

# ravel函数可以实现数组展平，跟reshape相反
print(b.ravel())
print(b)
# flatten函数功能同ravel
print(b.flatten())

# 元组来设置数组维度
b.shape = (2, 12)
print(b)

# 组合数组
# 有hstack和concatenate(axis=1)可以横向组合
# 有vstack和concatenate(axis=0)可以纵向组合
a = arange(8).reshape(4, 2)
c = arange(12).reshape(4, 3)
d = arange(6).reshape(2, 3)
print(c)
print(a)
print(d)
print(np.hstack((a, c)))
print(np.vstack((c, d)))
print(np.concatenate((a, c), axis=1))  # axis=1横向，axis=0纵向
print(np.concatenate((c, d), axis=0))
# print(help(np.vstack))

# 深度组合dstack,相同元组才能进行深度组合，类似两张纸沿着纵深方向重叠在一起
print(np.dstack((arange(9).reshape(3, 3), arange(9).reshape(3, 3))))

# 数组分割
e = arange(27).reshape(3, 3, 3)
print(e)
print(np.dsplit(e, 3))  # 深度切割
print(np.vsplit(e, 3))  # 垂直切割
print(np.hsplit(e, 3))  # 横向切割
