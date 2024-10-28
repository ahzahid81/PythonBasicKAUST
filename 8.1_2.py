import turtle
wn = turtle.Screen()

amy = turtle.Turtle()
amy.pencolor("pink")
amy.right(170)

colors = ["purple", "yellow", "orange", "pink", "purple", "yellow", "orange", "pink","purple", "yellow", "orange", "pink","purple", "yellow", "orange", "pink","purple", "yellow", "orange", "pink","purple", "yellow", "orange", "pink","purple", "yellow", "orange", "pink","purple", "yellow", "orange", "pink","purple", "yellow", "orange", "pink","purple", "yellow", "orange", "pink"]

for color in colors:
    if amy.pencolor() == "purple":
        amy.forward(50)
        amy.right(59)
        
    elif amy.pencolor() == "yellow":
        amy.forward(65)
        amy.left(98)
        
    elif amy.pencolor() == "orange":
        amy.forward(30)
        amy.left(60)
    elif amy.pencolor() == "pink":
        amy.forward(50)
        amy.right(57)
        
    amy.pencolor(color)
    
wn.exitonclick()