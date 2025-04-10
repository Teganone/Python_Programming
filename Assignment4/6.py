# 5）查找车牌号（20分）


import math

def find_license_plate():
    for i in range(1000, 10000):
        # 检查前两位数字是否相同
        if i // 1000 % 10 == (i // 100) % 10:
            # 检查后两位数字是否相同
            if i % 10 == (i // 10) % 10:
                # 检查整个数字是否为某个整数的平方
                if int(math.sqrt(i)) ** 2 == i:
                    return i

# 调用函数
plate_number = find_license_plate()

# 输出结果
if plate_number:
    print(f"车牌号是: {plate_number}")
else:
    print("没有找到符合条件的车牌号")


