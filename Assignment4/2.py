# 2）绘制空心正方形（10分）

def draw_hollow_squre(size):
    for i in range(size):
        if i == 0 or i == size - 1:
            print('* ' * size)
        else:
            print('* ' + '  ' * (size - 2) + '*')


size = int(input("请输入空心正方形的边长："))
draw_hollow_squre(size)