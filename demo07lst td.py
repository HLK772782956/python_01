# 列表推导式
# 需求：生成一个1-10的列表
lst = []
for x in range(1,11):
    lst.append(x)
print(lst)

lst1 = [x for x in range(1,11)]
print(lst1)

# 需求：生成一个1-10的列表,要求只打印奇数
lst2 = [x for x in range(1,11) if x % 2 != 0]
print(lst2)

# 需求：生成一个1-10的列表,生成的奇数值再加上10
lst3 = [x+10 for x in range(1,11) if x % 2 != 0]
print(lst3)

for y in range(1,11):
    print(y)