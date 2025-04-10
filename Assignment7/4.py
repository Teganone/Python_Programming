import turtle

length = 50
gap = 10
turtle.colormode(255)
colors = ['red',"orangered","orange", (253,198,11),"yellow", "yellowgreen", "green", (6,150,187), "blue", (68,78,153), "Purple", (196,3,125)]
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-400,0)
def draw_square(length):
    for i in range(4):
        pen.fd(length)
        pen.right(90)
    # pen.down()

for i in range(len(colors)):
    pen.pendown()
    pen.color(colors[i],colors[i])
    pen.begin_fill()  # 开始填充
    draw_square(length)
    pen.end_fill()
    pen.penup()
    pen.fd(gap+length)
turtle.mainloop()
