a = int(input("请输入第一个数字:"))
sign = input("运算符(+ - * /):")
b = int(input("请输入第二个数字:"))

if sign == "+":
    result = a + b
elif sign == "-":
    result = a - b
elif sign == "*":
    result = a*b
elif sign == '/':
    # 检查除数是否为0
    if b == 0:
        print("错误:除数不能为0。")
    else:
        result = a / b
else:
    print("错误:无效的运算符。")

if 'result' in locals():  # 确保变量result已经被定义
    print("运算结果:", result)

