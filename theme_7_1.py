import turtle
import random
options = ['Квадрат', 'Прямоугольник', 'Треугольник']
shape = random.choice(options)
if shape == 'Квадрат':
    t = turtle.Pen()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    turtle.exitonclick()
elif shape == 'Прямоугольник':
    t = turtle.Pen()
    t.forward(150)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(100)
    turtle.exitonclick()
elif shape == 'Треугольник':
    t = turtle.Pen()
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    turtle.exitonclick()