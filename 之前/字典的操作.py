#字典的添加/删除/修改/操作

#添加
thisdict =	{"brand": "Porsche","model": "911","year": 1963}
thisdict['money'] = 100
print(thisdict)

#删除
thisdict.pop('money')
del thisdict["year"]

#访问
print(thisdict["brand"])
print('brand' in thisdict)

#遍历
for x in thisdict.keys():
    print(x)
for x in thisdict.values():
    print(x)
for x in thisdict.items():  #会是元组形式
    print(x)
for x,y in thisdict.items():
    print(x,y)


#复制
mydict = thisdict.copy()
print(mydict)

#字典的嵌套
key1 = {'name':'Tom','year':2009}
key2 = {'name':'Annie','year':2011}
kids = {'kid1':key1,'kid2':key2}

print(kids)


#使用函数构建字典
fun_dict = dict(brand = 'Porsche',model = '911',color = 'red')
print(fun_dict)