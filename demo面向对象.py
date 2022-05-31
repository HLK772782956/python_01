
# 车的启动
def car_start():
    print('车进行启动')


# 车的驾驶


# 面向对象

# 1.定义一个电梯的类 ：class 类名
class Elevator():

# 2.在类的的里申明车的属性（数据）和方法（函数）
    button = '开/关'   #按钮
    floor = 15        #层数
    peple_nums = 13   #承载人数

    # 打开电梯
    def start(self):
        print('面向对象-打开电梯')
    # 关闭电梯
    def stop(self):
        print('面向对象-关闭电梯')
    # 运行电梯
    def run(self):
        print('面向对象-电梯运行')
# 3.定义一个具体的对象，叫初始化对象，对象是一个实实在在的对象 ：=》初始化对象：对象名 = 类名（）
e = Elevator()

# 4.使用对象调用方法或者属性 : 对象名.属性 / 对象名.方法
e.start()
e.stop()
e.run()

#  用函数去实现
# 打开电梯
def start():
    print('函数-打开电梯')

# 关闭电梯
def stop():
    print('函数-关闭电梯')

# 运行电梯
def run():
    print('函数-电梯运行')
start()
stop()
run()

# 类的定义
# class 类名()：
#   多个（≥0）类属性...
#   多个（≥0）类方法...