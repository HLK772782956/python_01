"""

def div(x,y):
    z = x / y
    return z
 print(div(3,4))
"""

"""
使用try....except语句
# 格式：
try:
    正常代码块
except Exception as e:
    处理异常代码块
"""
def div(x,y):
    try:
        z = x / y
        return z
    except Exception as e:        # 上面报错这里就打印异常
        print('除法不能出现被0除的情况')
print(div(3,4))
print(div(3,0))  # 正常这里是异常报错的


"""
# flinally语句
try:
    正常的代码块
finally:
    必须要处理的代码块    
"""
try:
    f = open('a.txt','r')
    lines = f.readline()
    for x in lines:
        print(y)      # 这里是异常报错的，正常下面的代码都无法运行
except Exception as e:
    print(e)

finally:              # 作用是不管是否报错，都会运行下面的代码块
    print('是否运行该区域')

