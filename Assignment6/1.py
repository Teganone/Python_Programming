print("今有一个数,")
x_3 = int(input("若用3除余数为:"))
x_5 = int(input("若用5除余数为:"))
x_7 = int(input("若用7除余数为:"))
ranges = 1000
res = [i for i in range(ranges+1) if i%3==x_3 and i%5==x_5 and i%7==x_7]
print(f"在0～{ranges}中有这样的数:\n{res}")
    