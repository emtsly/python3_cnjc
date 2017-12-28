# encoding=utf-8
c = '%u8FD9%u662F%u4E00%u4E32%u6587%u5B57'
# print("".join([(len(i)>0 and chr(int(i,16)) or "") for i in c.split('%u')]))
# print(c.split('%u'))


s = ''
# for i in c.split('%u'):  # 把编码按%u分割，获得各个字的编码
#     if len(i)>0:    # 如果当前字的编码不为空
        # print(chr(int(i,16)))  # 把16进制编码转换为整数，并获得对应的字符（汉字）

for i in c.split('%u'):
    # if len(i) > 0:
    temp = (len(i)>0 and chr(int(i,16)) or "")
        # print( temp )
    s.join(temp)

print(s)
print(type(s))

a = [(len(i)>0 and chr(int(i,16)) or "") for i in c.split('%u')]
# print(a)



# 二进制转换为整数，int的第二个参数是原进制
i = '1001'
print(int(i,2))

