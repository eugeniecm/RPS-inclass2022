


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#
import random
import os

#let the player input their names
username = os.getenv("username", default="Player One")

#ask for a use input 
user_choice = input("Hello! Please choose one: 'rock', 'paper', 'scissors': ")

print(username, "chose", user_choice)

# validation 
# include capitalization

user_choice = user_choice.lower()

if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    print("You have not chosen a valid option. Goodbye!")
    exit()

# computer choice
possible_choice = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_choice)

print("Computer chose", computer_choice)

#determine the winner
if user_choice == computer_choice:
    print("Both players played", user_choice, "It's a tie!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock.", username, "won! Congrats!")
    else: 
        print("Scissors cuts paper. You lost! It's ok.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper.", username, "won! Congrats!")
    else: 
        print("Rock crushes scissors. You lost! It's ok.")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock crushes scissors.", username, "won! Congrats!")
    else: 
        print("Paper covers rock. You lost! It's ok.") 

#final results 
print("Thanks for playing", username, "Please play again!")

