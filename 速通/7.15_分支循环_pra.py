# #例子1：100以内的素数
# for i in range (2, 101):
#     is_prime = True
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(i, end=' ')
#
# #斐波那契数列
# a , b = 0, 1
# for i in range(2, 10):
#     c = a + b
#     print(c)
#     a = b
#     b = c


# #例子3：寻找水仙花数
# for i in range(100, 999):
#     high = i // 100
#     middle = i //10 % 10
#     low = i % 10
#     if high ** 3 + middle ** 3 + low ** 3 == i:
#         print(i, end=' ')

# #正整数反转
# x = int(input("num = "))
# reverse_x = 0
# while x > 0:
#     reverse_x = reverse_x * 10 + x % 10
#     x = x // 10
# print(reverse_x)


import random

money = 1000
count = 0

while money > 0:
    print(f"\nYou have ${money}")
    bet = int(input("Your bet: "))

    while bet > money:
        print("Your bet is more than you have!")
        bet = int(input("Re-enter your bet: "))

    num = random.randint(2, 12)
    print("Dice rolled:", num)

    if num in [7, 11]:
        money += bet
        print("You win!")
    elif num in [2, 3, 12]:
        money -= bet
        print("You lose!")
    else:
        print("No result, money unchanged.")

    count += 1

print("\nGame over! You played", count, "rounds.")




