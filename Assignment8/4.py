import random

def PI(num_points):
    """
    使用蒙特卡罗方法计算π的近似值。

    参数:
    num_points (int): 要生成的随机点的数量

    返回:
    float: π的近似值
    """
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / num_points) * 4

# 测试函数
print(PI(1_000_000))  # 输出3.141988，注意每次计算结果不尽相同。
print(PI(100_000_000))  # 输出3.14153632