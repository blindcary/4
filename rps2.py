import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def player_choice():
    while True:
        player_choice = input("\nEnter...\nfor Rock 1\nfor Paper 2\nfor Scissors 3:\n\n")
        if player_choice in ["1","2","3"]:
            return int(player_choice)
        else:
            print("Invalid input, please enter 1,2 or 3.")
def computer_choice():
    return random.choice([1,2,3])