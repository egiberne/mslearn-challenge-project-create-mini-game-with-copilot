# Create a game where the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. 
# The interaction in the game will be through the console or terminal.
# The winner of the game is determined by three simple rules:
#- Rock beats scissors.
#- Scissors beat paper.
#- Paper beats rock.


# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# The game should end when the player decides to quit.
# The player should be able to see the score of the current game at any time.
# The game should be able to handle incorrect inputs and continue running.


import random

def game():
    print("Welcome to Rock, Paper, Scissors Game!")
    print("Enter your choice: rock, paper, or scissors")
    print("To quit the game, enter 'q'")
    print("To see the score, enter 'score'")
    print("")

    player_score = 0
    computer_score = 0

    while True:
        computer_choice = random.choice(["rock", "paper", "scissors"])
        player_choice = input("Enter your choice: ")

        if player_choice == "q":
            break
        elif player_choice == "score":
            print("Player: ", player_score)
            print("Computer: ", computer_score)
            continue
        elif player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        print("Computer: ", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "rock":
            if computer_choice == "scissors":
                print("You win!")
                player_score += 1
            else:
                print("Computer wins!")
                computer_score += 1
        elif player_choice == "scissors":
            if computer_choice == "paper":
                print("You win!")
                player_score += 1
            else:
                print("Computer wins!")
                computer_score += 1
        elif player_choice == "paper":
            if computer_choice == "rock":
                print("You win!")
                player_score += 1
            else:
                print("Computer wins!")
                computer_score += 1

    print("Final score:")
    print("Player: ", player_score)
    print("Computer: ", computer_score)


game()


 
