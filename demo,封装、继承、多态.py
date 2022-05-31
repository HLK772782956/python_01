#  封装 把类的部分方法和属性隐藏掉，通过在变量或方法前个单下划线(_)或双下划线(__)
class Students():
    name = '张三'
    __score = '60'

    def __set_score(self,score):
        self.__score = score

    def get_score(self):       # 这里是给了一个可以查看的接口，只能通过接口去查看隐藏的东西
        return self.__score
print(Students.name)
# print(Students.__score) #这里是无法生效的，因为__score已经隐藏
s = Students()    # 创建一个对象
print(s.get_score()) # 这样调用接口方法就可以查看到隐藏的分数
print('='*40)
# 类的继承
"""
1.必须具有父子关系，有父子关系
2.在子类可以直接调用父类中的方法（功能）或者属性（数据）
"""
class People():  # 父类
    age = 0
    def eat(self,people_tyge):
        print(people_tyge,'在吃饭')

class Students1(People):  # 括号内加上的类就是父类
    pass                  # 子类

class Teacher(People):    # 子类
    pass

s1= Students1()           # 创建一个对象
s1.eat('学生')             # 这里students没有写代码但是可以调用父类的方法
s1.age = 20               # 这里调用的是父类的age
print(s1.age)

t = Teacher()
t.eat('老师')
t.age = 40
print(t.age)



#  多肽
"""
1.必须是继承关系
2.子类的方法覆盖了父类的方法
"""
class People():  # 父类
    age = 0
    def eat(self,people_tyge):
        print(people_tyge,'在吃饭')

class Students2(People):
    def eat(self,grade):    # 子类的方法
        print(grade,'年级的学生在吃饭')
s2= Students2()
s2.eat('2')                 # 这里调用的就不是父类的方法而是子类的方法了
print('='*40)

# 还想用调用父类方法
class People():  # 父类
    age = 0
    def eat(self,people_tyge):
        print(people_tyge,'在吃饭')

class Students3(People):
    def eat(self,grade):                # 子类的方法
        super().eat(grade)              # 这里就是继承父类的功能
        print(grade,'年级的学生在吃饭')    # 这里是对功能的拓展

s3 = Students3()
s3.eat('张三')                       # 这里就是调用的父类的方法而不是子类的方法