#将一颗色子掷6000次，统计每种点数出现的次数

import random
num_1, num_2, num_3, num_4, num_5, num_6 = 0, 0, 0, 0, 0, 0

for i in range(6000):
    num = random.randint(1, 6)
    match num:
        case 1 : num_1 = num_1 + 1
        case 2 : num_2 = num_2 + 1
        case 3 : num_3 = num_3 + 1
        case 4 : num_4 = num_4 + 1
        case 5 : num_5 = num_5 + 1
        case 6 : num_6 = num_6 + 1
else:
    print(num_1, num_2, num_3, num_4, num_5, num_6)
