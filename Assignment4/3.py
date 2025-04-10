# 2）绘制空心菱形（20分）

def draw_hollow_diamond(size):
    for i in range(size):
        if i==0 or i==size-1:
            print(' '* (size//2)+'*')
        elif i <= size // 2:
            print(' ' * (size//2 - i) + '*' + ' ' * (2 * i - 1) + '*')
        else:
            print(' ' * (i - size // 2) + '*' + ' ' * (2 * (size - i - 1) - 1) + '*')
    
draw_hollow_diamond(11)
