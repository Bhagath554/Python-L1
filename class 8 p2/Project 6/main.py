import turtle

t = turtle.Turtle()
s = turtle.Screen()

colors = ['orange','red','green','yellow','blue','purple','indigo']


s.bgcolor('black')
t.speed('fastest')
t. hideturtle()

while True:
    for x in range(200):
        t.pencolor(colors[x%len(colors)])

        t.width(x/100 + 1)

        t.forward(x)
        t.left(90)
   
