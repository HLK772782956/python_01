# 函数 ：具有特定的功能的代码块。比如说登录功能，相加

# 函数的定义 ：加法
def add(x,y):    # x,y代表参数
    z = x+ y
    return z

# 函数的调用
print(add(3,4))
print(add(3,4.2))
print(add('a','b'))

# 位置参数
# 主要是指调用函数时的参数数量和位置要和定义的形参中的一致。传多或传少都会报
# 异常(TypeError)。
print(add(3,4))     # 3的值传入x，4的值传入y
print(add('hello','world'))  # hello的值传入x，world的值传入y
# print(add(3)) 报错，因为只有一个X的值，少了y值

# 关键字参数
# 以key=value形式，key代表函数中的形参名称，value就是传递给函数的实际
# 的值
def student_lesson(grade,subject):
    z = "{}年级上{}课".format(grade,subject)
    return z
print(student_lesson(2,'语文'))  #位置参数
print(student_lesson(grade=2,subject='语文'))  #关键字参数
print(student_lesson(subject='语文',grade=2))  #关键字参数可以调换位置
print(student_lesson(6,subject='体育'))  # 位置参数和关键字参数混合使用

# 默认参数 ：如果函数调用时，传递的实际参数经常会是一个值，那我们就可以给这个参数设置默认值 。如果设置默
# 认参数，需将在位置参数后
def study_language(name,language='python'):
    info = ("{}要学习{}语言".format(name,language))
    return info

print(study_language('张三','java'))
print(study_language('李四','python'))
print(study_language('王五'))      # 这里没有编写语言的值但还是正常打印出来，因为函数内设置了语言的默认值

# 可变化参数 ：

# 定义列表形式
def add(x,y,*args):
    print(args)   # 可以看到args的值是什么，也可以不打印
    z = x+y + sum(args)
    return z
print(add(3,4))          # 可变化参数也可以不传入数据
print(add(3,4,5))        # 传递一个参数
print(add(3,4,5,6,7,8))  # 传递多个参数

# 使用列表的方式进行调用
print(add(3,4,*[5,6,7,8]))  # 传递列表

# 字典形式的参数
def show_info(**kwargs):
    print(kwargs)

print(show_info(a='hello',b='world',c=123))
print(show_info(a='hello',b='world'))
dt_data = {'x':1,'y':2,'z':3}
print(show_info(**dt_data))

def show_info1(*args,**kwargs):   # 此函数可以接收任何长度，任何位置，任何关键字的参数
    print(args,kwargs)

