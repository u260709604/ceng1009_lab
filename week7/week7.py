# #exercise 1
# #def sumTo(n)
# #total = n*(n*(n+1)) / 2
# #return total
#
#
# #exercise 2
# import turtle
# # def drawStar(t, n):
# #     if n< 3 or n % 2 == 0:
# #         print()
# #
# #   for in i range:
# #       t
#
#
#
# #exercise3
#
#  #def sumTo(n):
#  #     total = 0
#  #     for i in range(1, n+1):
#  #         total += i
#  #     return total
#  #
#  # print(sumTo(10))
#  #
#  # n = int(input())
#  # print(sumTo(n))
#
#
#
#
#
#  #exercise 4
# import math
#
# #
# # def mySqrt(x):
# #     guess = x/2
# #     for i in range(20):
# #         guess = (1/2) * (guess + x / guess)
# #     return guess
# #
# # n = int(input("enter a positive integer"))
# # print(mySqrt(n))
#
#
# #exersise 5
#
# import turtle
# import week6
# from week6.week6 import drawSprite
# from week6.week6 import drawEquitriangle
#
#
#
#
# # def fancySquare(t, size):
# #     for corner in range(4):
# #         drawSprite(t, 8, 20)
# #         t.forward(size)
# #         t.left(90)
# #
# # wn = turtle.Screen()
# # wn.bgcolor("lightgreen")
# #
# # t = turtle.Turtle()
# # t.color("hotpink")
# # t.pensize(2)
# # fancySquare(t, 100)
# #
# # wn.exitonclick()
# # import turtle
# #
# # def drawTip(t,size):
# #     t.begin_fill()
# #     t.left(90)
# #     t.forward(size/2)
# #     t.right(120)
# #     t.forward(size)
# #     t.right(120)
# #     t.forward(size)
# #     t.right(120)
# #     t.forward(size/2)
# #     t.right(90)
# #     t.end_fill()
# #
# # def drawSpriteWithTips(someturtle, legs, length):
# #     angle = 360 / legs
# #     for i in range(legs):
# #         someturtle.forward(length)
# #         drawTip(someturtle, 10)
# #         someturtle.backward(length)
# #         someturtle.left(angle)
# #
# #
# #
# #
# #
# # def fancySquare(t, size):
# #     for corner in range(4):
# #         drawSpriteWithTips(t, 8, 20)
# #         t.forward(size)
# #         t.left(90)
# #
# #
# # wn = turtle.Screen()
# # wn.bgcolor("black")
# #
# #
# # t = turtle.Turtle()
# # t.color("white")
# #
# # t.pensize(2)
# #
# # fancySquare(t, 100)
# # wn.exitonclick()
#
#
#
#
# #exercise 6

# def checkNumber(n):
#     if n > 0:
#         return "Positive"
#     if n < 0:
#         return "Negative"
#     else:
#         return "Zero"
#
# n = int(input("Enter a number: "))
# print(checkNumber(n))




#exercise 7
# import turtle
#
# def drawBar(t, height, gap):
#     t.penup()
#     t.left(90)
#     t.forward(height+gap)
#     t.write("  "+ str(height))
#     t.back(height+gap)
#     t.rigt(90)
#     t.pendown()
#
#
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
#
# def barChart(data):
#     maxheight = max(data)
#     numbars = len(data)
#
#     border = 10
#
#     gap = (maxheight+border)/25
#
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#     right = 40 * numbars + border
#     top = maxheight + 4 * border
#     wn.setworldcoordinates(-border, -border, right, top)
#
#     t = turtle.Turtle()
#     t.color("blue")
#     t.fillcolor("red")
#     t.pensize(3)
#
#
#     for height in data:
#         drawBar(t, height, gap)
#
#     wn.exitonclick()
#
#
#  data = [48, 117, 200, 240,160, 260, 220]
#  barChart(data)