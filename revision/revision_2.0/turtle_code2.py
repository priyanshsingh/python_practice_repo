import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.setup (width=1920, height=1080, startx=0, starty=0)

s.bgcolor("black")
t.width(2)
t.speed(15)
col = ("#039fbe", "#e8d21d", "#cf1578")

for i in range(1000):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)
    