# Random Color CRASH Infinity

coins=0
import random
color=["Red","Yellow","Green","Blue","Orange","Purple","Aqua","Lime","White","Light Blue"]
while True:
    colors=random.choice(color)
    predict=input("Predict the next color. ")
    if predict == colors:
        print("Good Job!")
        print("The color was:", colors)
    else:
       print("Nope! Choose Again!")
       print("The color was:", colors)
    if colors == "Red":
        print("You lost! You got Red.")
        break
    elif colors == "Light Blue":
        print("You got 1 coin.")
        coins = 1 + coins
        print("You have",coins,"coins, way to go!")
