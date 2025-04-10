import turtle


turtle.title("科赫曲线")
turtle.setup(800,400)
pen = turtle.Turtle()
pen.penup()
pen.goto(-300,-70)
pen.shapesize(2)
pen.pendown()
def koch(size,n):
    if n==0:
        pen.fd(size)
    else:
        for angle in [0,60,-120,60]:
            pen.left(angle)
            koch(size/3,n-1)

koch(600,3)
# 保持窗口打开直到用户关闭
turtle.mainloop()