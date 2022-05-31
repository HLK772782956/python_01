# 字符串格式化
# 格式化字符 ：%s
my_str = "my name is %s" % ("张三")
print(my_str)
# 格式化整数 ：%d
my_str1 = "张三今年%d岁" % (25)
print(my_str1)
# 格式化浮点数 ：%f
my_str2 = "一斤苹果%f钱" % (3.5)
print(my_str2)
my_str3 = "一斤苹果%f钱" % (3.4572)
print(my_str3)


# m.n : m是显示的最小总宽度，n是小数点后的保留位数
my_str4 = "一斤苹果%5.2f钱" % (3.789)
print(my_str4)
# 显示左对齐 ：-
my_str5 = "一斤苹果%-7.2f钱" % (3.789)
print(my_str5)
# 数字前面显示加号 ：+
my_str6 = "一斤苹果%+7.8f钱" % (3.789)
print(my_str6)
# 前面使用0代替 ：0
my_str7 = "一斤苹果%07.2f钱" % (3.787)
print(my_str7)


# 使用format去格式化 ："{}".format("字符串")
#my_str8 = "张三今年%d岁" % (25)
my_str8 = "张三今年{}岁".format(25)
print(my_str8)

# format格式化两个参数 ："{} {}".format(参数1,参数2)
my_str9 = "今天星期{},张三买了{}斤苹果".format('一',5)
print(my_str9)
my_str10 = "今天周{},李四买了{}件衣服".format('二',3)
print(my_str10)

# format的位置参数 ： "{}{}{}".format(第一个数，第二个数，第三个数)
my_str11 = "今天星期{0},张三买了{1}斤苹果".format('五',3)
print(my_str11)

# format的关键字参数 ："{}{}".format(x='hello',y='world')
my_str12 = "今天星期{x},张三买了{y}斤苹果".format(y='2',x='五')
print(my_str12)

# 位置参数和关键字参数结合使用 ：
