#**要求**：某公司有三种类型的员工，分别是部门经理、程序员和销售员。
# 需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。
# 其中，部门经理的月薪是固定 15000 元；程序员按工作时间（以小时为单位）支付月薪，每小时 200 元；
# 销售员的月薪由 1800 元底薪加上销售额 5% 的提成两部分构成。


# class Employee:
#     def __init__(self, name):
#         self.name = name
#         self.__salary = 0
#
#     def set_salary(self, salary_amount):
#         self.__salary = salary_amount
#
#     def get_salary(self):
#         print(f"{self.name}的工资是{self.__salary}")
#
# class Manager(Employee):
#     def __init__(self, name):
#         super().__init__(name)
#         self.set_salary(15000)
#
# class Programmer(Employee):
#     def __init__(self, name, work_hours):
#         super().__init__(name)
#         self.work_hours = work_hours
#         self.set_salary(self.cal_salary())
#
#     def cal_salary(self):
#         return self.work_hours * 200
#
# class Saler(Employee):
#     def __init__(self, name, sales):
#         super().__init__(name)
#         self.sales = sales
#         self.set_salary(self.cal_salary())
#
#     def cal_salary(self):
#         return self.sales * 0.05 + 1800
#
#
# manager1 = Manager("horton")
# manager1.get_salary()
#
# programmer1 = Programmer("Tom",80)
# programmer1.get_salary()
#
# saler1 = Saler("Tom", 200000)
# saler1.get_salary()


#最推荐的写法

class Employee:
    def __init__(self, name):
        self.name = name
        self._salary = 0  # protected 属性，更灵活
        self.calculate_salary()

    def calculate_salary(self):
        raise NotImplementedError("子类必须实现 calculate_salary 方法")

    def get_salary(self):
        print(f"{self.name}的工资是{self._salary}元")

class Manager(Employee):
    def calculate_salary(self):
        self._salary = 15000

class Programmer(Employee):
    def __init__(self, name, work_hours):
        self.work_hours = work_hours
        super().__init__(name)  # 注意 work_hours 需要先设定
    def calculate_salary(self):
        self._salary = self.work_hours * 200

class Saler(Employee):
    def __init__(self, name, sales):
        self.sales = sales
        super().__init__(name)
    def calculate_salary(self):
        self._salary = 1800 + self.sales * 0.05


e1 = Manager("Alice")
e2 = Programmer("Bob", 120)
e3 = Saler("Carol", 50000)

e1.get_salary()
e2.get_salary()
e3.get_salary()