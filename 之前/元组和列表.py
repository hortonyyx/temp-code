#元组可以包含不同的数据类型（整数、字符串、列表、字典和另一个元组）

my_tuple = (1, "hello", [3, 4, 5], {"key": "value"}, (6, 7))
print(my_tuple)

#对元组解包——快速赋值
a,b,c,d,e = my_tuple
print(a,b,c,d,e)

#列表也能包含多种元素
list_a = ['twenty_twenty', 1, '14th']
print(len(list_a))
list_a += [1,2]
print(list_a)

#列表的添加，替换与删除
list_a.append('end')
list_a.insert(1,'inserted')
list_a[0] = 'begin'
list_a.remove(1)
list_a.pop(-2)
del list_a[0]
print(list_a)
