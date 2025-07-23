class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 私有属性，表示账户余额

    # 公共方法，供外部调用
    def deposit(self, amount):
        self.__add_balance(amount)
        print(f"存入: {amount}, 当前余额: {self.__balance}")

    # 私有方法，用于更新余额
    def __add_balance(self, amount):
        self.__balance += amount

# 创建对象
account = BankAccount(1000)

# 尝试直接调用私有方法
account.__add_balance(500)  # 会报错：AttributeError: 'BankAccount' object has no attribute '__add_balance'

# 正确的调用方式，通过公共方法间接调用私有方法
account.deposit(500)  # 输出: 存入: 500, 当前余额: 1500
