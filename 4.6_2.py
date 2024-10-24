import turtle
wn = turtle.Screen()
jose = turtle.Turtle()
jose.shape("turtle")
jose.penup()

for _ in range (10):
    jose.forward(50)
    jose.stamp()
    jose.forward(-50)
    jose.right(36)
    
wn.exitonclick()