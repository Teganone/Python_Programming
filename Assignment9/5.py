def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 计算并输出12月兔子对数
lst = list(map(fibonacci,range(1,13)))
print(f"12个月后的兔子对数：{lst}")