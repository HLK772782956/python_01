# 实例: 创建学生类，要求有属性：姓名和年级 ; 方法有：学习的方法，打印学生的上课情况
class Students():

    name = ''
    grade = ''

    def study(self):
        print('{}年级的学生{}正在学习'.format(self.grade,self.name))

s1 = Students()
s1.name = '张三'
s1.grade= '5'
print(s1.study())

s2 = Students()
s2.name = '李四'
s2.grade = '4'
print(s2.study())
s2.study()

print('='*30)
# 类的变量
class Students():

    name = '张三'  # 这就是类变量
    grade = '1'   # 这就是类变量

    def study(self):
        print('{}年级的学生{}正在学习'.format(self.grade,self.name))

# 使用类名去调用
print(Students.name) #Students 就是类名的意思
print(Students.grade)

# 使用实例化对象去调用
s = Students()  #s 就是实例化对象
print(s.name)
print(s.grade)

# 实例变量
class Students():

   # name = ''
   # grade = ''

    def study(self):
        self.name = '王五'   # 这就是实例变量（在方法内使用）
        self.grade ='3年级'  # 这就是实例变量
        print('{}年级的学生{}正在学习'.format(self.grade,self.name))

class Students1():
    def study(self):
        self.a ='赵六'
        self.b = '王五'
        print(self.a,'在干嘛',self.b,'在干嘛')


 # def study(self):
  #  score = 60      # 这就是局部变量'变量名=值',只能在方法内使用