
"""
# 循环语句
for循环的语法格式如下:
for 循环变量 in 序列
代码块
"""
for y in "abcde":
    print(y)


#while循环

#打印1-5
print("===============")
a = 1
while a <= 5:
    print(a)
    a+=1

#计算1-100的和
sun = 0
a = 1

from loguru import logger

# range函数
"""
range(start,end,step)
start：代表数列的开始索引，包括开始索引。此参数若省略，默认从0开始
end：代表数列的结束索引，不包括结束索引，必填
step:步长，每次跳跃的步数 。此参数若不填写，默认步长为1
示例：打印1~10的数字
"""
print("====================")
for x in range(1,10,1):
    print(x)

print("===========================")
# break语句断开循环
# 需求: 循环1-10，当遇到7退出循环
for x in range(1,11,1):
    print(x)
    if x == 7:
        break
print("============================")
# continue语句进行跳出本次循环
# 需求 ： 循环1-10，当遇到7跳过该次循环
for x in range(1,11,1):
    if x == 7:
        logger.info(x)
        continue
    print(x)


# 列表list
# 格式 ：变量名 = []
alst = []  #定义空列表
blst = [11,23,'hlk',None]