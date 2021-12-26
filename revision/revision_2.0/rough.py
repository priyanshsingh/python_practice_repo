import turtle
from random import randint

TUrt = turtle.Turtle()
s = turtle.Screen()

s.Turtle.bgcolor('black') #Set the background color
 Turtle.colormode(255) #Set color mode
 Turtle.width = 1 #Set the brush width
 Turtle.speed(0) #Set the brush speed 0 is the fastest
cnt = 0
x = 0
while x<400:
         r = randint(0,255) # 
    g = randint(0,255)
    b = randint(0,255)
         Turtle.pencolor(r,g,b)#Set brush color
         # Each line length +1 rotates 91° to the right
    turtle.forward(50+cnt)
    cnt += 1
    x += 1
    turtle.right(91)
 
 