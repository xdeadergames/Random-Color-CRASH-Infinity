# Random Color CRASH Infinity

coins=0
import random
import pickle
color=["Red","Yellow","Green","Blue","Orange","Purple","Aqua","Lime","White","Light Blue"]
while True:
    colors=random.choice(color)
    with open("coins.dat", "wb") as file:
        pickle.dump(coins, file)
    with open("coins.dat", "rb") as file:
        coins = pickle.load(file)
    predict=input("Predict the next color. ")
    if predict == colors:
        print("Good Job!")
        print(f"The color was: {colors})
    else:
       print("Nope! Choose Again!")
       print(f"The color was: {colors})
    if colors == "Red":
        print("You lost! You got Red.")
        break
    elif colors == "Light Blue":
        print("You got 1 coin.")
        coins = 1 += coins
        print(f"You have {coins} coin(s), way to go!")
    
