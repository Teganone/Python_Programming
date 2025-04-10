import turtle


# 创建画笔
pen = turtle.Turtle()
# pen.speed(0)  # 设置画笔速度为最快

def draw_half_circle(radius,angle,fill_color):
    pen.color('black',fill_color)
    pen.begin_fill()
    pen.circle(radius,angle)
    pen.end_fill()

# 绘制太极图
def draw_tai_chi():
    draw_half_circle(100, 180, 'black')
    draw_half_circle(100, 180, 'white')
    # 绘制小的白色半圆
    pen.penup()
    pen.goto(0, 100)  # 移动到小的白色半圆的起始位置
    pen.pendown()
    draw_half_circle(50, 180, 'white')
    # 绘制小的黑色半圆
    pen.penup()
    pen.goto(0, 100)   # 移动到小的黑色半圆的起始位置
    pen.pendown()
    draw_half_circle(50, 180, 'black')

# 调用函数绘制太极图
draw_tai_chi()

# # 隐藏画笔
pen.hideturtle()

# 保持窗口打开直到用户关闭
turtle.mainloop()