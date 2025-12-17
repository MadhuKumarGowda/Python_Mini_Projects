"""
Roll Dice Game Project
Author: Madhu Kumar K S
Date: December 16, 2025
Description: A dice rolling game where 2-4 players take turns rolling dice to reach a target score.
Players lose their turn score if they roll a 1, but can choose to stop and bank their points.
"""

import random

def roll():
    """Roll a six-sided die and return the result"""
    min_value = 1
    max_value = 6
    return random.randint(min_value,max_value)

# Get number of players (2-4)
while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players count must be between 2 - 4")
    else:
        print("Invalid Entry, try again")

# Initialize game settings
max_score = 50
player_score = [0 for _ in range(players)]

# Main game loop
while max(player_score) < max_score:

    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1} turn has just started.\n")
        print(f"your total score is {player_score[player_idx]}\n")
        current_score = 0

        # Player's turn loop
        while True:
            should_roll = input("Would you like to roll (y) ?")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("you rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"you rolled a {value}")
            
            print("Your score is:", current_score)
        
        # Add current turn score to total
        player_score[player_idx] += current_score
        print(f"Your total score is: {player_score[player_idx]}")

# Determine winner
max_score = max(player_score)
winning_idx = player_score.index(max_score)
print(f"Player number {winning_idx + 1} is the winner with {max_score}")