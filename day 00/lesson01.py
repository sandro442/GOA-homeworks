from turtle import *


#  we want to paint house

# step 1 draw a sssquare
width(7)
speed(100)

color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

# end of square 


#draw door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

end_fill()

# roof
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# draw window 1

begin_fill()
color("brown")

penup()
goto(15,100)
pendown()

left(120)
forward(40)
left(90)
forward(60)

left(90)
forward(40)
left(90)
forward(60)

end_fill()

#window 2

begin_fill()
color("brown")


left(90)
penup()
goto(185,100)
pendown()

left(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)

end_fill()




exitonclick()
