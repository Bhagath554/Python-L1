import turtle

turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()

sc.setup(400,300)

turtle.title("Welcome to Turtle Window")

board = turtle.Turtle()


for i in range(5):
    board.forward(50)

    board.right(90)


    i = i+1

