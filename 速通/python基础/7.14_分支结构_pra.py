# 例子2：百分制成绩转换成等级
score = int(input("请输入成绩(0-100): "))
match score:
    case score if score < 60:
        grade = 'E'
    case score if 60 <= score < 70:
        grade = 'D'
    case score if 70 <= score < 80:
        grade = 'C'
    case score if 80 <= score < 90:
        grade = 'B'
    case score if 90 <= score <= 100:
        grade = 'A'
    case _:
        print("输入错误！")
print("成绩等级为：", grade)


# 例子3：计算三角形的周长和面积
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print(f'周长: {perimeter}')
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'面积: {area}')
else:
    print('不能构成三角形')





