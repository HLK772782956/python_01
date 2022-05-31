# 模块
# 1.导入 ；有两种导入方式
# 1.全部导入：inport 模块的名字
import demo1        # 调用demo1的方法
demo1.add(3,5)      # demo1里的加法被调用
demo1.acc(3,5)      # demo1里的减法被调用

# 2.使用模块的某一个功能时，通过form 模块名 import 成员名（方法，类，功能）
from demo1 import add
print(add(4,6))     # 这里只调用了demo1里的加法

from demo1 import People
demo1.People()      # 这里调用了demo1里的类

# 导入其他包下的模块
from python_02.hlk import add  #这里导入的是python02下的hlk模块的加法
print(add(6,6))
print('='*40)

# os 模块
import os

print(os.listdir())     # 返回当前路径下的所有文件

print(os.getcwd())      # 返回当前的工作目录
print('='*40)

# datetime 模块
import  datetime

print(datetime.datetime.now())
print('='*40)

# sys 模块
import sys
print(sys.path)
print('='*40)


# 下载第三方包
# 使用pip命令可以下载第三方的包
# pip install 包名
