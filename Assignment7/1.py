# 1.绘制500条直线（20）
import turtle

# 设置画布和画笔
screen = turtle.Screen()
pen = turtle.Turtle()

# 设置画笔速度为最快
pen.speed("fastest")

# 循环绘制500条直线
for i in range(1, 501):
    # 绘制长度为i的直线
    pen.forward(i)
    # 向右旋转91度
    pen.right(91)

# 隐藏画笔
# pen.hideturtle()

# 保持窗口打开直到用户关闭
screen.mainloop()

