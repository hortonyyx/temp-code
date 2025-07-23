# BMI 
# height = float(input("请输入身高(m): "))
# weight = float(input("请输入体重(kg): "))
# BMI = weight / (height ** 2)
# print("BMI指数为: ", BMI)
# if BMI < 18.5:
#     print("体重过轻")
# elif 18.5 <= BMI < 24:
#     print("体重正常")
# elif 24 <= BMI < 28:
#     print("体重过重")
# elif 28 <= BMI < 32:
#     print("肥胖")
# else:
#     print("严重肥胖")

# match-case语法实现分支结构
status_code = int(input('响应状态码: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)

# case match合并模式
# status_code = int(input('响应状态码: '))
# match status_code:
#     case 400 | 405: description = 'Invalid Request'
#     case 401 | 403 | 404: description = 'Not Allowed'
#     case 418: description = 'I am a teapot'
#     case 429: description = 'Too many requests'
#     case _: description = 'Unknown Status Code'
# print('状态码描述:', description)


x = int(input('请输入一个整数: '))
y1 = x +2
y2 = x * 5 -1
y3 = x ** 2
match x:
    case x if x < 1:
        print(y1)
    case x if 1 <= x < 10:
        print(y2)
    case x if x >= 10:
        print(y3)