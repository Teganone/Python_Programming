# # 1）绘制倒三角形（10分）


def draw_inverted_triangle(width):
    for i in range(width):
        print('*' * (width-i))

draw_inverted_triangle(9)