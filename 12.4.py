
def pythonsum(n):
    a = list(range(n))  # 不同于2.x，3.x中的range返回的是range类型，不是list类型，所以需要强制转换
    b = list(range(n))
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c


print(pythonsum(6))

import numpy as np


def numpysum(n):
    a = np.arange(n) ** 2  # arange返回的是一个数据
    b = np.arange(n) ** 3  #
    c = a + b
    return c


print(numpysum(6))

# 效率比较
from datetime import datetime  # 这样调用的是datetime.datetime(),下面就可以直接用datetime.now()了
size = 1000

start1 = datetime.now()
c = pythonsum(size)
delta1 = datetime.now() - start1
print('the last two element of the pythonsum:', c[-2:])
print('the time of numpy:', delta1.microseconds)

start2 = datetime.now()
d = numpysum(size)
delta2 = datetime.now() - start2
print('the last two element of the numpy:', d[-2:])
print('the time of numpy:', delta2.microseconds)

from numpy import arange

def typeing():
    a = arange(5)
    b = a.dtype  # dtype获取数组元素的类型
    d = a.shape  # shape获取数组的形状，即行数和列数
    c = np.shape([[1, 2],
              [3, 4],
              [5, 6]])
    print(b, c, d)

typeing()



e = np.array([np.arange(2), np.arange(2)])
print(e)


# 初始化数组的几种办法
def oringal(x, y):
    print(np.zeros((x, y)))
    print(np.empty([x, y]))   #empty返回无意义的数值
    print(np.ones([x, y]))
oringal(4,5)

a = np.array([[1, 2], [3, 4]])
print(a.astype(np.float), a.astype(np.int32))         # 通过astype安全转换数组元素类型
print(np.float64(62), np.bool(20))                 # 也可以普通转换数组元素类型

# try异常处理
def aa(obj, index):
    print(obj[index])


x = 'spam'
try:
    aa(x, 5)
except IndexError:
    print('go to exception')