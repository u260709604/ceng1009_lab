#import random
#for _ in range(10):
    #print(random.randint())

#for _in in range(1,11):
    #print(random.randint(25, 35))
#import math
#side_a = 3.0
#side_b = 4.0
#

# def areaOfcircle(r):
#return math.pi * (r**2)
#radius = 5
#print(area(radius))





import turtle

def drawSquare(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)
window = turtle.Screen()
window.bgcolor("lightgreen")
t = turtle.Turtle()
t.color("hotpink")
t.pensize(3)

for _ in range(5):
    drawSquare(t, 20)
    t.penup()
    t.backward(20)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.pendown()



for i in range(20, 120, 20):
    drawSquare(t, 20)


screen.exitonclick()