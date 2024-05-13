from turtle import *
import turtle
#Time stamp April 03, 2024 Time: 17:08
##CE1126 - little rectangles, #1EB53A - bottom flag, #FFFFFF - middle flag.

# page setup
setup(1056, 704)
speed(0)
bgcolor("#0099B5")
#This is where the stars will be drawn
#specific_spots = [(-260, 160), (-200, 160), (-140, 160), (-80, 160), (-20, 160), (-200, 230), (-140, 230), (-80, 230), (-20, 230), (-140, 300), (-80, 300), (-20, 300)]

# Function to draw one star
def solid_star(size):
    print("filling star")
    begin_fill()
    color("white")
    for i in range(5):
        forward(size)
        left(72)
        forward(size)
        right(144)
    end_fill()

speed(0)
color("white", "white")
penup()

specific_spots = [(-260, 160), (-200, 160), (-140, 160), (-80, 160), (-20, 160), (-200, 230), (-140, 230), (-80, 230), (-20, 230), (-140, 300), (-80, 300), (-20, 300)]

for spot in specific_spots:
    x, y = spot
    penup()
    goto(x, y)
    pendown()
    solid_star(13)
    
# Moon - Part 1
penup()
goto(-340, 140)
pendown()
color("white")
begin_fill()
circle(85)
end_fill()

# Moon - Part 2
penup()
goto(-305, 155)
pendown()
color("#0099B5")
begin_fill()
circle(70)
end_fill()

#Turtle creation 1
t = turtle.Turtle()
turtle.setup(width = 1056, height = 704)
#Speed of turtle
t.speed(5)
#The dimensions of the rectangle
length = 1056
width = 25
#Tell the turtle where to go
t.penup()
t.goto(-528, 120)
t.pendown()

#Fill the rectangle with the color of your choice
t.fillcolor("#CE1126")
#start/end the fill. 
t.begin_fill()
#Time to draw the rectangle
for i in range(2):
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)

t.end_fill()

#Turtle creation 2
t = turtle.Turtle()
turtle.setup(width = 1056, height = 704)
#Speed of turtle
t.speed(5)
#The dimensions of the rectangle
length = 1056
width = 25
#Tell the turtle where to go
t.penup()
t.goto(-528, -120)
t.pendown()

#Fill the rectangle with the color of your choice
t.fillcolor("#CE1126")
#start/end the fill. 
t.begin_fill()
#Time to draw the rectangle
for i in range(2):
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)

t.end_fill()

#Turtle creation 3
t = turtle.Turtle()
turtle.setup(width = 1056, height = 704)
#Speed of turtle
t.speed(5)
#The dimensions of the rectangle
length = 1056
width = 215
#Tell the turtle where to go
t.penup()
t.goto(-528, 95)
t.pendown()

#Fill the rectangle with the color of your choice
t.fillcolor("#FFFFFF")
#start/end the fill. 
t.begin_fill()
#Time to draw the rectangle
for i in range(2):
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)

t.end_fill()

#Turtle creation 4
t = turtle.Turtle()
turtle.setup(width = 1056, height = 704)
#Speed of turtle
t.speed(5)
#The dimensions of the rectangle
length = 1056
width = 215
#Tell the turtle where to go
t.penup()
t.goto(-528, -145)
t.pendown()

#Fill the rectangle with the color of your choice
t.fillcolor("#1EB53A")
#start/end the fill. 
t.begin_fill()
#Time to draw the rectangle
for i in range(2):
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)

t.end_fill()

hideturtle()
done()
