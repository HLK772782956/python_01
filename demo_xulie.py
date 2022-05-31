# 语法：
# 变量名 = []
#说明：定义列表需要使用[],[]内可以存放任何的数据类型
#实例
alst = []
blst = [1,11.1,'hlk',None]
print(alst)
print(blst)

# 循环列表
#语法：
#for 元素 in 列表:
# 代码块
for x in blst:
    print("列表中的值:",x)


print("==========================================")


# 列表的方法 ：
clst = ['red','green','blue']

# 向列表中添加元素 ：list.append(obj),列表的元素
clst.append('black')
print("加入black后的结果:",clst)

# 列表翻转 ：list.reverse()
clst.reverse()
print("翻转后的结果:",clst)

# 统计在列表中出现的次数 ： list.count(obj)
print(clst.count('blue'))

# 从列表中找出某个元素的位置 : list.index(obj)
print(clst.index('red'))

# 向列表的某个位置插入元素 ：list.insert(index,obj)
clst.insert(1,'pink')
print(clst)

# 列表排序 : list.sort(),里面的元素必须是同类的
#clst.sort()
#print("排序后的结果:“,clst)

print('=========================================')


for x in [1,2,3,4,5,6,7,8,9,10]:
    print(x)


