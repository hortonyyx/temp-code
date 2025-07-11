class People:
    total_amount = 0

    def __init__(self,name,age,gender,salary):
        self.name = name
        self.__gender = gender 
        self.__age = age 
        self.__salary = salary  #定义了两个私有属性
        People.total_amount += 1
    
    def get_gender(self):
        if self.__gender == 0:
            return 'female'
        elif self.__gender == 1:
            return 'male'
        else:
            return 'error'
    
    def get_age(self):
        return self.__age
    def get_salary(self):
        return self.__salary
    #定义了三个公共方法，供外部调用来访问私有属性

    def __add_salary(self,money):
        if money > 0:
            self.__salary += money
        else:
            print('must > 0')
    #定义了私有方法，需要通过类内部再创建方法调用

    def raise_salary(self,money):
        self.__add_salary(money)
        print(f'now the total salary is {self.__salary}')
    #定义公共方法

    def __del__(self):
        People.total_amount -= 1
        print(f'now the total amount is {People.total_amount}')

tom = People('tom',32,1,5000)
peter = People('peter',26,1,10000)
alice = People('alice',19,0,4500)
marry = People('marry',48,0,6000)

print(tom.name)
print(peter.get_age())
print(alice.get_gender())
print(marry.get_salary())

print(People.total_amount)
del marry
print(People.total_amount)

alice.raise_salary(2000)



        
        