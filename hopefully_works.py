# Importing the random library
import random

# Adding the code to create a list containing the three actions of the game
actions = ["rock", "paper", "scissors"]

# Adding the code to set the scores of players to 0
score_of_player1 = 0
score_of_player2 = 0

# Adding the code to ask the user how many rounds they want to play
how_many_iterations = int(input("How many times do you want to play? Give us a number = "))

# Writing a for loop and put the game inside
for i in range(how_many_iterations):

    # Adding the code to select a random action for each player
    choice_of_player1 = random.choice(actions)
    choice_of_player2 = random.choice(actions)

    # Adding the code to print the players choices
    print("The choice of Player 1 is " + choice_of_player1)
    print("The choice of Player 2 is " + choice_of_player2)

    is_winner = 0

    if choice_of_player1 == "paper" and choice_of_player2 == "rock":
        is_winner = choice_of_player1
        print("Paper beats rock!")
    elif choice_of_player1 == "rock" and choice_of_player2 == "paper":
        is_winner = choice_of_player2
        print("Paper beats rock!")
    elif choice_of_player1 == "paper" and choice_of_player2 == "scissors":
        is_winner = choice_of_player2
        print("Scissors beats paper!")
    elif choice_of_player1 == "scissors" and choice_of_player2 == "paper":
        is_winner = choice_of_player1
        print("Scissors beats paper!")
    elif choice_of_player1 == "rock" and choice_of_player2 == "scissors":
        is_winner = choice_of_player1
        print("Rock beats scissors!")
    elif choice_of_player1 == "scissors" and choice_of_player2 == "rock":
        is_winner = choice_of_player2
        print("Rock beats scissors!")
    elif choice_of_player1 == choice_of_player2:
        print("You have chosen same thing, this means EQUALITY.")

    # Printing the winner of this round
    if is_winner == choice_of_player1:
        print("The winner of this round is Player 1!")
        score_of_player1 += 1
    else:
        print("The winner of this round is Player 2!")
        score_of_player2 += 1

# Printing the score
print("Total score of the Player 1 is " + str(score_of_player1) + " and total score of the Player 2 is " + str(
    score_of_player2) + ".")
if score_of_player1 > score_of_player2:
    winner = "Player 1"
    print("So the winner is " + winner)
elif score_of_player1 < score_of_player2:
    winner = "Player 2"
    print("So the winner is " + winner + "!")
else:
    print("The game ended in a " + str(score_of_player1) + "-" + str(score_of_player2) + "draw.")
