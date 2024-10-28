import turtle

wn = turtle.Screen()

amy = turtle.Turtle()
amy.pencolor("pink")

if amy.pencolor() == "pink":
    amy.left(60)
    amy.forward(100)
    
else:
    amy.right(60)
    amy.forward(100)
    

kenji = turtle.Turtle()

if kenji.pencolor() == "pink":
    kenji.left(60)
    kenji.forward(100)
    
else:
    kenji.right(60)
    kenji.forward(100)
    


wn.exitonclick()