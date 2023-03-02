import turtle
turtle.setposition(0, 0)
turtle.bgcolor("black")
feb_21 = turtle.Turtle()
feb_21.pencolor("white")
feb_21.pensize(3)
feb_21.speed(5)

feb_21.left(90)
feb_21.forward(150)
feb_21.right(30)
feb_21.forward(80)
feb_21.left(120)
feb_21.forward(150)
feb_21.left(120)
feb_21.forward(80)
feb_21.right(30)
feb_21.forward(150)

feb_21.pencolor('black')
feb_21.right(90)
feb_21.forward(50)
feb_21.pencolor('white')
feb_21.right(90)
feb_21.forward(120)
feb_21.left(70)
feb_21.forward(60)
feb_21.left(110)
feb_21.forward(140)
feb_21.right(90)

feb_21.pencolor('black')
feb_21.forward(50)
feb_21.pencolor('white')
feb_21.right(90)
feb_21.forward(120)
feb_21.left(70)
feb_21.forward(60)
feb_21.left(110)
feb_21.forward(140)
feb_21.right(90)

# left side 1st
feb_21.pensize(.5)
feb_21.goto(50, 0)
feb_21.pensize(3)
feb_21.left(-90)
feb_21.forward(120)
feb_21.right(70)
feb_21.forward(60)
feb_21.right(110)
feb_21.forward(140)

feb_21.pencolor('black')
feb_21.left(90)
feb_21.pencolor('black')
feb_21.forward(50)

feb_21.pencolor('white')
feb_21.left(90)
feb_21.forward(120)
feb_21.right(70)
feb_21.forward(60)
feb_21.right(110)
feb_21.forward(140)

# Pen move on left side
feb_21.right(90)

feb_21.pensize(.5)
feb_21.forward(170)

# move for circle create
feb_21.pencolor('black')
feb_21.goto(-35, 190)
feb_21.pencolor('white')

feb_21.begin_fill()
feb_21.circle(60)
feb_21.color('#FF0000')
feb_21.end_fill()

feb_21.pencolor('white')
feb_21.pensize(1)
feb_21.right(90)
feb_21.forward(30)
feb_21.right(180)
feb_21.forward(220)

feb_21.left(90)
feb_21.forward(20)
feb_21.left(90)
feb_21.forward(220)

feb_21.left(90)
feb_21.forward(40)
feb_21.left(90)
feb_21.forward(220)

feb_21.left(90)
feb_21.forward(20)


turtle.mainloop()
