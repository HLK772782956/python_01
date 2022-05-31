# 序列的通用操作
# 索引 - 列表，序列，元组，字符串
lst = ['red',10,12.3,'blue']
print(lst[1])   # 列表里的第二个值
print(lst[-1])

tp = ('red',10,12.3,'blue') #元组
print(tp[1])
print(tp[-1])

astr = 'sadasda12'   #字符串
print(astr[1])
print(astr[-1])

# 序列切片 ：seq[wtart:end:step]
# start：表示切片的开始索引位置（包括该位置），此参数也可以不指定，默认为 0，也就是从列表
# 的开头进行切片；
# end：表示切片的结束索引位置（不包括该位置），如果不指定，则默认为列表的长度，注意end
# 不能超过列表的长度，否则会报错；
# step：表示切片的步长，如果 step 的值大于 1，则在进行切片操作时，会“跳跃式”的取元素。如
# 果省略设置 step 的值，step的值就为1，则最后一个冒号就可以省略。
lst1 = ['red',10,12.3,'blue',5,'black']
print(lst1[1:5:1]) # 获取第2个到第5个元素
print(lst1[0:5:2]) # 获取偶数的值

tp1 = ('red',10,12.3,'blue',6,'black') #元组
print(tp1[1:5:1])
print(tp1[0:5:2])

bstr = 'dsadasda133' #字符串
print(bstr[1:5:1])
print(bstr[0:5:2])

lst2 = ['red',10,12.3,'blue',5,'black']
print(lst2[::1])
print(lst2[0:6:1])

print(lst2[2::])
print(lst2[2:6:1])

print(lst2[1::2])
print(lst2[1:6:2])

# 列表中有10个元素，让你取出其中奇数个数的元素
print(lst2[0::2])

# 列表的相加和相乘
alst = [1,2]
blst = [3,4]
print(alst+blst)
print(alst*2) #alst的内容翻倍

clst = [None] * 3  # []里面的默认长度是10
print(clst)

print('====================')
print('=' * 30) #便捷的方法

# 检查元素 ： in
lst5 = ['red',10,12.3,'blue',5,'black']
print('pink' in lst5)
print(10 in lst5)

# 序列中的方法 ：list()
# dlst = [] 序列转化列表
dlst = list()
print(dlst)
cstr = 'abc' # 字符串转化列表
elst = list(cstr)
print(elst)

# 循环序列中的索引和值
for index,vls in enumerate(lst5):
    print(index,'======',vls)

qlst = [1,2,3]
dstr = str(qlst)
print(dstr)