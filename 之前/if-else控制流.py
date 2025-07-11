import time
for i in range(0,11):
    print(i)
    time.sleep(1)

#综合小练习

customers = {'Tom':15,'Trent':22,'Bob':30,'Talor':65}
for x,y in customers.items():
    if y < 18:
        print(x + ", it's half for you")
    elif y < 60:
        print(x + ", sorry, no discount for you")
    else:
        print(x + ", it's free for you")