# Create a python code where the computer is your opponent and can randomly choose one of the elements (rock, paper, or scissors) 
# the winner of the game is determined by three simple rules:
# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
# Your interaction in the game will be through the console or Terminal.


import random
# Create a list of play options
t = ["Rock", "Paper", "Scissors"]
# Assign a random play to the computer
computer = t[random.randint(0,2)]
# Set player to False
player = False
while player == False:
    # Set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[random.randint(0,2)]



 

 


 

