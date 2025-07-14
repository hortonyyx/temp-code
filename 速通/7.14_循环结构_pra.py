

# import time
# #用_作循环变量逼格更高
# for _ in range(10):
#     time.sleep(1)
#     print("Hello, world!")

# # 1——100偶数求和

# sum = 0
# for _ in range(2, 101, 2):
#     sum += _
# print("1-100偶数求和结果:", sum)

# # 1——100的和:while循环
# total = 0
# i = 1
# while i <= 100:
#     total += i
#     i += 1
# print(total)


#break和continue

# total = 0
# i = 2
# while True:
#     total += i
#     i += 2
#     if i > 100:
#         break
# print(total) 

# total = 0
# for i in range(1, 101):
#     if i % 2 != 0:
#         continue
#     total += i
# print(total)

# # 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{i}×{j}={i * j}', end='\t')
#     print()


# # 例子1：判断素数
# num = int(input('请输入一个正整数: '))
# end = int(num ** 0.5)
# is_prime = True
# for i in range(2, end + 1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(f'{num}是素数')
# else:
#     print(f'{num}不是素数')


# #例子2：最大公约数
# a = int(input('请输入第一个正整数: '))
# b = int(input('请输入第二个正整数: '))
# if a > 0 and b > 0:
#     for i in range(min(a, b), 0, -1):
#         if a % i == 0 and b % i == 0:
#             print(f'最大公约数是: {i}')
#             break
# else:
#     print('请输入正整数')


# 例子3：猜数字游戏
import random
random_num = random.randint(1, 100)
attempts = 0
num = int(input('请输入一个1-100之间的整数: '))
while num != random_num:
    attempts += 1
    if num < random_num:
        print('猜小了，请再试一次')
    else:
        print('猜大了，请再试一次')
    num = int(input('请输入一个1-100之间的整数: '))
print(f'恭喜你猜对了！你总共猜了{attempts}次')
print(f'正确的数字是: {random_num}')