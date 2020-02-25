import turtle

#We setup the screen
wn = turtle.Screen()
wn.setup(width = 1.0, height = 1.0)
wn.bgcolor("black")

#We setup our drawing turtle
bob = turtle.Turtle()
#We give him some features
bob.speed(0)
bob.ht()
bob.color("white")
bob.setheading(90)

forward = 3
color = ["blue", "green", "yellow", "orange", "red", "purple"]

for x in range (500):
    bob.color(color[x%6])
    bob.width(x/100+1)
    bob.fd(x)
    bob.rt(59)
    
