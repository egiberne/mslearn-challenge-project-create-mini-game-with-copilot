# Create a python code where the computer is your opponent and can randomly choose one of the elements (rock, paper, or scissors) 
# the winner of the game is determined by three simple rules:
# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
# Your interaction in the game will be through the console or Terminal.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.

import random

def game():
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    computer_score = 0
    while True:
        player = input("Rock, Paper, or Scissors? ").lower()
        computer = random.choice(["rock", "paper", "scissors"])
        print(f"Computer: {computer}")
        if player == computer:
            print("It's a tie!")
        elif player == "rock":
            if computer == "scissors":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player == "scissors":
            if computer == "paper":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player == "paper":
            if computer == "rock":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        else:
            print("Invalid input!")
        print(f"Player: {player_score} | Computer: {computer_score}")
        if input("Play again? (y/n): ") != "y":
            print("Thanks for playing!")
            break

game()

# Run the code in the terminal
# python app.py

