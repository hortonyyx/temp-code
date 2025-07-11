#加到自己
def func_sum_to(n):
    if n > 0:
        result = n + func_sum_to(n-1)
    else:
        result = 0
    return result

print(func_sum_to(10))

#计算阶乘
def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n*factorial(n-1)
    return result

print(factorial(6))


#斐波那契数列
def func_Fibonacci(i):
    if i == 1:
        result = 1
    elif i == 2:
        result = 1
    else:
        result = func_Fibonacci(i-1) + func_Fibonacci(i-2)
    return result

print(func_Fibonacci(8))



#汉诺塔问题
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print('move disk ' + str(n) + 'from ' + source + ' to ' + target)
    else:
        hanoi(n-1,source, auxiliary, target)
        #把n-1移到auxiliary上
        print('move disk ' + str(n) + 'from ' + source + ' to ' + target)
        #把n移到target上
        hanoi(n-1,auxiliary,target,source)

hanoi(5,'A','C','B')