from turtle import *

background_color = 'red'
pen_color = 'red'
color(pen_color,background_color)
begin_fill()


for i in range(5):
    left(72)
    forward(100)
    right(144)
    forward(100)

end_fill()
hideturtle()
done()