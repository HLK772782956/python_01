# 文件读写步骤
# 1 打开文件：open(filename,mode) # filename代表文件名，mode代表读写模式
f = open('a.txt','r')

# 2 读取文件：read()
result = f.read()
print(result)

# 3 关闭文件：close()
f.close()

# 写文件
# 1.打开文件：open()
g = open('a.txt','w')

# 2.写内容：write()
g.write('hello python')

# 3 关闭文件：close()
g.close()

# 按行读取文件内容
#1.打开文件
h = open('b.txt','r')

# 2.按行读取 ：readline
while True:
    line = h.readline()
    print(line)
    if not line:
        break

# 3.关闭文件：close()
h,close