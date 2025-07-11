#在字典中，如果多个键相同，最后一个赋值会覆盖之前的值
key_1 = 'Jack'
key_2 = 'Jack'

dict_a = {key_1:1234,key_2:4321,'Rose':0000}
print(dict_a)
#这里为：{'Jack': 4321, 'Rose': 0}  字典中不允许重复键
print(dict_a['Jack'])

dict_a['Tom'] = 1111
print(dict_a)

#字典的‘键——对’关系
a = dict_a.keys()
b = dict_a.values()
x,y,z = dict_a.items()
print(x,y,z)#这里是把键——对以元组的形式一对对赋给xyz

names = dict_a.keys()
print(names)
print(type(names))#这是一个视图对象
names_list = list(names)#转化成列表
print(names_list)