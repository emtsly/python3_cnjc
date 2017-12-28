# encoding=utf-8
# 把JavaScript用escape编码的字符串转换为汉字
c = '%u8FD9%u662F%u4E00%u4E32%u6587%u5B57'
print("".join([(len(i)>0 and chr(int(i,16)) or "") for i in c.split('%u')]))

# join的参数是一个迭代
# [(len(i)>0 and chr(int(i,16)) or "") for i in c.split('%u')]是一个迭代
# 由c按'%u'切割后的item 迭代
# 每个item做判断len(item)>0 时，把item当做16进制数转换为整数，再转换为字符
# 把每次迭代的结果写入字符串



print(c.split('%u'))