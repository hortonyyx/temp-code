#假设有一段楼梯，共有 n 级台阶。每次你可以选择迈一步或两步。编写一个递归函数，计算你有多少种不同的方式可以爬上这段楼梯。

def func_sum_step(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return func_sum_step(n-2) + func_sum_step(n-1)
    
print(func_sum_step(10))
