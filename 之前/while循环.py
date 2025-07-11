import time

a = 0
b = 1
x = 0
while x < 100:
    x = a + b
    a = b
    b = x
    print(x)
    time.sleep(1)

#循环的跳过与退出
a = 0
b = 1
x = 0
while x < 500:
    x = a + b
    a = b
    b = x
    if x%2 == 0:
        continue
    print(x)
    if x%11 == 0:
        break
    time.sleep(1)