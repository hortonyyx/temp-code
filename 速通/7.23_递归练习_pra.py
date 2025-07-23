# #走楼梯
#
# def Func_stairs(num):
#     if num == 1:
#         func_num = 1
#     elif num == 2:
#         func_num = 2
#     else:
#         func_num = Func_stairs(num - 1) + Func_stairs(num - 2)
#     return func_num
#
# print(Func_stairs(5))
# print(Func_stairs(3))
# print(Func_stairs(20))
#
#
# #阶乘问题
#
# def Func_jiechen(num):
#     if num == 1:
#         func_num = 1
#     elif num == 2:
#         func_num = 2
#     else:
#         func_num = num * Func_jiechen(num - 1)
#     return func_num
#
# print(Func_jiechen(5))

# #汉诺塔问题
# amount = 0
# def hanoi(n, source, target, auxiliary):
#     global amount
#     if n == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         amount += 1
#     else:
#         hanoi(n-1, source, auxiliary, target)
#         print(f"Move disk {n} from {source} to {target}")
#         amount += 1
#         hanoi(n-1, auxiliary, target, source)
#
#     return amount
#
# # hanoi(4, "A", "B", "C")
# print(hanoi(5, "A", "B", "C"))

def F(n,s,t,a):
    if n == 1:
        print(f"Move disk 1 from {s} to {t}")
    else:
        F(n-1,s,a,t)
        print(f"Move disk {n} from {s} to {t}")
        F(n-1,a,t,s)

