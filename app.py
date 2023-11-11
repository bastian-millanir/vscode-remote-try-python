#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# Write 'Hello, world' in the console
print("Hello, world")

# Code a minigame about rock, paper, scissors in Python where the user plays against the computer and each round the player is asked to choose between rock, paper, or scissors. The computer chooses randomly. After a round is over, the user should be asked if they want to play again. If they do, the game starts over. If they don’t, the game ends and the final scores are printed. The game should keep track of the score during the game and print it out after each round. The game should also keep track of the number of rounds played. The game should end when the user chooses to stop playing. The game should also print out the number of rounds played at the end of the game.
# Write your code here
import random
import sys

def play(): 
    user_score = 0
    computer_score = 0
    rounds = 0
    while True:
        user_choice = input("Choose rock, paper, or scissors: ")
        computer_choice = random.choice(["rock", "paper", "scissors"])
        if user_choice == computer_choice:
            print("Tie!")
        elif user_choice == "rock":
            if computer_choice == "paper":
                print("Computer wins!")
                computer_score += 1
            else:
                print("You win!")
                user_score += 1
        elif user_choice == "paper":
            if computer_choice == "scissors":
                print("Computer wins!")
                computer_score += 1
            else:
                print("You win!")
                user_score += 1
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("Computer wins!")
                computer_score += 1
            else:
                print("You win!")
                user_score += 1
        else:
            print("Invalid input.")
            continue
        rounds += 1
        print("Score: You {} - {} Computer".format(user_score, computer_score))
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            continue
        else:
            print("Thanks for playing!")
            print("Rounds played: {}".format(rounds))
            break

play()