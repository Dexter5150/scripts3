from numpy import arange
from numpy import array
import numpy as np
m=array([arange(2),arange(2)])
print(m.shape)
n=array([[arange(3),arange(3)],[arange(3),arange(3)]])
print(n.shape)

# 多维数组的切片
# reshape改变维度

b=arange(24).reshape(2,3,4)
print(b)
print(b[:,0,0])
print(b[...,0])        # 多个冒号可以用省略号代替
print(b[...,0][0,:])   # 多次索引只要有效就可以
print(b[0,1,:])
print(b[0,1,::2])      # 间隔选定元素

# ravel函数可以实现数组展平，跟reshape相反
print(b.ravel())
print(b)
# flatten函数功能同ravel
print(b.flatten())

# 元组来设置数组维度
b.shape=(2,12)
print(b)



# 组合数组
# 有hstack和concatenate(axis=1)可以横向组合
# 有vstack和concatenate(axis=0)可以纵向组合
a=arange(8).reshape(4,2)
c=arange(12).reshape(4,3)
d=arange(6).reshape(2,3)
print(c)
print(a)
print(d)
print(np.hstack((a,c)))
print(np.vstack((c,d)))
print(np.concatenate((a,c),axis=1))   # axis=1横向，axis=0纵向
print(np.concatenate((c,d),axis=0))
# print(help(np.vstack))

# 深度组合dstack,相同元组才能进行深度组合，类似两张纸沿着纵深方向重叠在一起
print(np.dstack((arange(9).reshape(3,3),arange(9).reshape(3,3))))


# 数组分割
e=arange(27).reshape(3,3,3)
print(e)
print(np.dsplit(e,3))       # 深度切割
print(np.vsplit(e,3))       # 垂直切割
print(np.hsplit(e,3))       # 横向切割

# 数组的转换
b=np.array([2,3,4.+3.j])
c=np.array([1,2,3,4,5])
print(b)
print(b.tolist())    # tolist转换数组为列表
print(b.tostring())  # tostring转换数组为字符串
print(c.tostring())
# print(np.fromstring('\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10@\x00\x00\x00\x00\x00\x00\x08@'))
b = np.array([ 1.+1.j,  3.+2.j])
print(b.tostring())
# print(np.fromstring('\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x00@'))
#  fromstring有疑问
#print(b.astype(int))



import math
print(np.arange(10))
print(np.sqrt(a))    # 对数组中的数字进行开方
print(np.exp(a))     # 对数组中的元素返回e^x的值
print(math.e**2)
# print(math.exp(b))   # 这样是不行的，注意

from numpy.random import randn

# print(randn(8))  # 返回一组具有正态分布的样本
x=randn(8)
y=randn(8)
print(x)
print(y)
print(np.maximum(x,y))   #对两组样本逐位比较，取最大值，返回一组新的样本

print(randn(4)*4)
print(np.modf(randn(4)*4))    # np.modf把一组数据的整数和小数分开，返回两个数组
print(math.modf(3.5541))     # math.modf把一个数字的整数和小数分开，返回一个元组

###利用数组进行数据处理
# np.meshgird函数
print(arange(5,6,0.01))   #按0.01步进划分，返回一个数组，
x=arange(4)
y=arange(5)
x,y=np.meshgrid(x,y)    # 返回两个二维数组，第一个以x为行，y的列维度，第二个以y的转置为列，x的行维度
print(x,y)

#
import matplotlib.pyplot as plt
import pylab
xs=arange(4)
ys=arange(4)
xs,ys=np.meshgrid(xs,ys)
print(xs,ys)
z=np.sqrt(xs**2+ys**2)
print(z)

plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
pylab.show()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.draw()


#将条件逻辑表达为数组运算
xarr= arange(1,2,0.1)
yarr= arange(2,3,0.1)
cond=array([True,False,True,True])

result=([x if c else y
         for x,y,c in zip(xarr,yarr,cond)])
print(result)
#np还有自带的更快且方便的函数where
result=np.where(cond,xarr,yarr)     #(条件c,结果x,结果y)= if c :x ; else: y
print(result)