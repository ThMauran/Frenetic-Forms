import turtle

s = turtle.Screen()
s.bgcolor("black")
s.setup(width = 1.0, height = 1.0)

t = turtle.Turtle()
t.speed(0)
t.color("white")
t.ht()

color = ["red", "green", "purple", "pink", "orange", "blue", "yellow", "white"]

for i in range(360):
    t.color(color[i%7])
    t.fd(i)
    t.lt(50)
    t.width(i/100+1)
