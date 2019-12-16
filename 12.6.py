# 面向对象

# 以下展示了__init__（）方法的特殊性，实例化的时候自动调用
class myclass1:
    def f(self, m1, m2):
        self.r = m1  # 错误，无法像__init__直接自动调用
        self.p = m2

    i = 12345


try:
    x = myclass1.f(23, 32)
    print(x.f)
except TypeError:
    print("错误，无法像__init__直接自动调用")


class myclass2:
    def __init__(self, n1, n2):
        self.a = n1  # __init__自动调用
        self.b = n2

    l = 12345


y = myclass2(23, 32)  # 实例化的时候自动调用
print(y.a)  # 实例化的时候自动调用


# 类的方法与普通函数
# 类的方法与普通函数只有一个区别，类的方法它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
class eg:
    def prt(self):
        print(self)
        print(self.__class__)


y = eg()
y.prt()  # self返回当前对象的地址，self.__class__指向类


# 类的方法
class Introduce:
    _weight = 0  # 定义私有属性，类外部无法直接访问

    def __init__(self, n, a, w):
        self.name = n
        self._weight = w
        self.age = a

    def prt(self):
        print("我叫%s,今年%d岁,体重%d公斤" % (self.name, self.age, self._weight))


z = Introduce('Dexter', 35, 70)
z1 = Introduce('Meya', 34, 60)
z.prt()
z1.prt()


# 单继承
class student(Introduce):
    def __init__(self, n, a, w, g):
        Introduce.__init__(self, n, a, w)  # 调用父类构造函数
        self.grade = g

    def prt(self):  # 覆写父类的方法
        print("我叫%s,今年%d岁,体重%d公斤,就读%d年级" % (self.name, self.age, self._weight, self.grade))


z2 = student('Dexter', 35, 70, 6)
z2.prt()


# 多继承
class speaker:
    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def sp(self):
        print('我叫%s，我是一个演说家，我演讲的题目是%s' % (self.name, self.topic))


class sample(speaker, student):
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


z3 = sample('Spange Bob', 17, 20, 9, '\'我爱蟹黄堡\'')
z3.prt()  # 如果调用的方法名字相同，默认会选择在父类中排序靠前的类的方法
z3.sp()


# 类的方法重写
# 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法
class father:
    def pp(self):
        print('\n此次调用了父类的方法')


class child(father):
    def pp(self):
        print('此次调用了子类的方法')


c = child()
c.pp()
super(child, c).pp()  # super:用子类的对象来调用被覆盖了的父类方法，相当于重写后的还原


class test:
    def __init__(self):
        self.sam1 = 1

    def www(self):
        print(self.sam1)


qq = test()
qq.www()


# 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):                                 # 返回对象
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, ss1):                            # add运算符重载，定义了一个方法：若相同类的实例化对象进行加法运算，会进行什么运算
        return Vector(self.a + ss1.a, self.b + ss1.b)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = Vector(5, 6)
print(v1 + v2 + v3)    # 可以多个类实例化对象相加，类中的__add__()不需要多传入形参
