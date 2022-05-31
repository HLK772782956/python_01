# 字符串方法演示
# 连接字符串 ：join('seq')
astr = '+'
bstr = astr.join('world')
print(bstr)
# 分割字符串 ：split(str="")
cstr = 'helloworld'
dstr = cstr.split('o')
print(dstr)
# 查找字符串 ：find(substr),如果找到了返回的是最小索引,没有找到返回-1
estr = 'hellowrold'
print(estr.find('l'))
print(estr.find('x'))
print(estr.index('l'))
# 查找以xxx结尾的字符串 ：endswith('xxx')
fstr = '测试报告.doc'
if fstr.endswith('.doc'):
    print('他是一个world文档')
# 替换字符串 ： replace(old_value,new_value)
gstr = 'hello,world'
print(gstr.replace('world','python'))

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
astr = 'sjklad 21343#$%sda3'
zf = 0
kg = 0
sz = 0
other = 0
for x in astr:
    if x.isalpha():
        zf += 1
    elif x.isdigit():
        sz += 1
    elif x.isspace():
        kg += 1
    else:
        other += 1
print('字符个数',zf)
print('数字个数',sz)
print('空格个数',kg)
print('其他个数',other)