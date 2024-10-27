fruits = ["apple", "orange", "banana", "cherry"]


for afruit in fruits:
    print(afruit)


print("This will execute first")

for _ in range(3):
    print("This line will execurte three times")
    print("This line will also execute three times")
    
print("Now we are outside of the for loop!")

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for i in [0, 1, 2, 3]:
    alex.forward(50)
    alex.left(90)
    
wn.exitonclick()

