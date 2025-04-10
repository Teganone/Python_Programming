import random
n = int(input("请输入正整数n:"))

# 设置随机种子以确保结果可复现
random.seed(0)

# 生成随机整数列表，
random_list = [random.randint(0, 99) for _ in range(n)]

# 打印原始列表
print("初始的:", random_list)

# 交换元素
random_list_reverted = random_list[::-1]
# 打印交换后的列表
print("交换后:", random_list_reverted)