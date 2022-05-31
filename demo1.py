def add(x,y):    # x,y代表参数
    z = x+ y
    return z
print(add(3,4))


def acc(a,b):    # x,y代表参数
    c = a - b
    return c
print(acc(3,4))

class People():  # 父类
    def eat(self,people_tyge):
        print(people_tyge,'在吃饭')
p = People()
print(p.eat('我和家人'))