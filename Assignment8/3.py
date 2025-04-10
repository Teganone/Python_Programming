def sum_of_factorials(n):
    if n==1 or n==0: 
        return 1
    return factorial(n) + sum_of_factorials(n-1)


def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)


# 从用户获取输入
N = int(input("请输入不大于10的正整数: "))

# 确保输入的数不大于10
if N > 10:
    print("输入的数不能大于10，请重新输入。")
else:
    # 计算并打印结果
    result = sum_of_factorials(N)
    if(N>2):
        print(f"1!+2!+...+{N}!={result:,}")
    else:
        pri = ''
        for i in range(1,N):
            pri += f"{i}!+"
        print(f"{pri}{N}!={result:,}")
        