import turtle

s = turtle.Screen()
s.bgcolor("black")
s.setup(width = 1.0, height = 1.0)

bob = turtle.Turtle()
bob.speed(0)
bob.ht()
color = ["blue", "green", "orange", "red"]

for i in range(360):
    bob.color(color[i%4])
    bob.fd(i*3)
    bob.lt(91)
    bob.width(i/100+1)
    
