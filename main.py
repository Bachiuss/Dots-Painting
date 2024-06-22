# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract("hirstpainting.jpg", 30)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)
import turtle
import random

turtle.colormode(255)
dummy = turtle.Turtle()
dummy.speed("fastest")
dummy.penup()
dummy.hideturtle()
color_list = [(142, 77, 52), (188, 165, 118), (165, 152, 38), (16, 46, 83), (46, 110, 135), (144, 57, 83),
              (61, 120, 100), (143, 184, 174), (141, 170, 176), (86, 36, 30), (65, 152, 168), (219, 209, 96),
              (109, 38, 32), (102, 145, 110), (166, 98, 130), (95, 122, 169), (161, 140, 160), (176, 104, 84),
              (52, 52, 87), (206, 182, 195), (67, 47, 63), (75, 51, 67), (174, 200, 193), (171, 200, 203),
              (217, 180, 172), (182, 191, 206)
            ]

dummy.setheading(225)
dummy.forward(300)
dummy.setheading(0)
number_of_dots = 101

for i in range(1, number_of_dots):
    dummy.dot(20, random.choice(color_list))
    dummy.forward(50)

    if i % 10 == 0:
        dummy.setheading(90)
        dummy.forward(50)
        dummy.setheading(180)
        dummy.forward(500)
        dummy.setheading(0)



screen = turtle.Screen()
screen.exitonclick()