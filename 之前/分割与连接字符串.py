#分割与连接字符串
string_b = 'info.tsinghua.edu.cn'
splitted_b = string_b.split('.')
print(splitted_b)
print(type(splitted_b))

joined_b = ' '.join(splitted_b)
print(joined_b)

#字符串是数组，单个字符就是长度为 1 的字符串