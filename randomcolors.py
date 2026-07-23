# Random Color CRASH Infinity

import random
color=["Red","Yellow","Green","Blue","Orange","Purple"]
while True:
    colors=random.choice(color)
    predict=input("Predict the next color.")
    if predict == colors:
        print("Good job!")
        print("The color was:", colors)
    else:
       print("Choose again!")
       print("The color was:", colors)
    if colors == "Red":
        print("You lost!")
        break