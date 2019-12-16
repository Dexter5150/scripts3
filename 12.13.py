
import numpy as np
from numpy import arange
import matplotlib.pyplot as plt
import pylab
from numpy.random import randn
xs=arange(-5,5,0.1)
ys=arange(-5,5,0.1)
xs,ys=np.meshgrid(xs,ys)
print(xs,ys)
z=np.sqrt(xs**2+ys**2)
print(z)


plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()                      # 附上一个数字颜色块用来参考
pylab.show()
plt.title('Image plot of $\sqrt{x^2 + y^2}$ for a grid of values')   # 标题未显示出来？？？
plt.draw()

print(randn(4,4))

