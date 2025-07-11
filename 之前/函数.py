#创建函数
def function_1():
    print('function hello')
#调用函数，需要加括号
function_1()

#参数和默认参数
def function_2(name):
    print(name + '!')
function_2('horton')
function_2('tom')


def function_3(country = 'China'):
    print('I come from ' + country)
function_3('England')
function_3()

#用list传参
def function_4(foods):
    for x in foods:
        print(x)

my_foods = ['apple','banana','grape','melon']
function_4(my_foods)

#关键字传参，相当于是写函数不用管，调用的时候指定清楚就行
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Phoebe", child2 = "Jennifer", child3 = "Rory")

#任意参数
def my_function2(*kids):
  print("The youngest child is " + kids[0])

my_function2("Phoebe", "Jennifer", "Rory")