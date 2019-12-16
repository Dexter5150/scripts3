def pythonsum(n):
    a = list(range(n))      # 不同于2.x，3.x中的range返回的是range类型，不是list类型，所以需要强制转换成列表
    b = list(range(n))
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c


print(pythonsum(5))
