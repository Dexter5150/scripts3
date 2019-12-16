# 迭代器与生成器

# 迭代器可以记住遍历的位置的对象
# 迭代器智能往前遍历知道所有元素完结，不能后退


print([x for x in 'spam'])  # 列表的简单迭代

a = [1, 2, 3, 4]  # 内置函数iter()创建迭代对象，next()输出迭代器的下一个元素
it = iter(a)
print(next(it))
print(next(it))
print([x for x in it])  # for语句成功的接上了next的遍历

for x in iter([1, 2, 3, 4]):  # for语句对迭代对象遍历的的另一种方式
    print(x, end='')


# 注意：列表自己不是一个迭代器，以下语句皆错
# print(next(x for x in 'spam'))  # 无法记住遍历的位置
# print(next(x for x in 'spam'))
# print(next([1, 2, 3, 4]))  # 列表自己不是迭代器，不能用next()


# 把类作为一个迭代器

class mynumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = mynumber()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))


# StopIteration:用于标识迭代的完成，防止无线循环。
class mynumber2:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 9:
            x = self.a
            self.a += 1
            return x
        else:  # 防止无线循环。在完成指定的循环次数后触发，然后结束迭代
            raise StopIteration


myclass1 = mynumber2()
myiter2 = iter(myclass1)
for x in myiter2:
    print(x)

# yield生成器
# 使用了yield的函数被称为生成器（generator）
# 调用一个生成器函数，返回一个迭代器对象

import sys


def fibonacci(n):
    c, d, counter = 0, 1, 0
    while True:
        if counter > n:
            return        # 记住，不带参数的return相当于返回NONE
        yield c           # yield当做return使用，并且将函数变成一个迭代器：停止此次运算，知道next()输出时，从上次停止的位置继续进行
        c, d = d, c + d   # 注意，这里跟c=d,d=c+d有很大区别，切记赋值运算先算右边
        counter += 1


f = fibonacci(10)
while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        sys.exit()
