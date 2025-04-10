def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def goldbach_conjecture(even_number):
    """
    验证哥德巴赫猜想。

    参数:
    even_number (int): 需要验证的大于2的偶数

    返回:
    list: 两个素数的列表，它们的和等于even_number。
    """
    if even_number%2 ==1:
        print("输入非偶数，请重新输入")
        return None
    for i in range(2, even_number):
        if is_prime(i) and is_prime(even_number - i):
            return [i, even_number - i]
    return None

# 从用户获取输入
even_number = int(input("请输入一个大于2的偶数: "))

# 验证哥德巴赫猜想
result = goldbach_conjecture(even_number)
if result:
    print(f"{even_number} = {result[0]} + {result[1]}")
else:
    print("没有找到符合条件的两个素数。")