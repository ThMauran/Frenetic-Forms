import turtle

s = turtle.Screen()
s.setup(width = 1.0, height = 1.0)
s.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.pu()
t.setposition(0,-50)
t.pd() 
t.setheading(60)
t.color("white")
t.ht()

color = ["red", "orange", "yellow"]

for i in range (181):
    t.color(color[i%3])
    t.fd(i*3.3+70)
    t.lt(121)
    t.width(i/50+1)
 
