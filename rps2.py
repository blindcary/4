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

def winner(player,computer):
    if(player==RPS.ROCK.value and computer==RPS.SCISSORS.value) or \
        (player==RPS.PAPER.value and computer==RPS.ROCK.value) or \
        (player==RPS.SCISSORS.value and computer==RPS.PAPER.value):
                return "🎉You win!"
    elif player == computer:
        return "😲Tie"
    else:
        return "🐍Python wins!"

def main():
    playagain = True
    while playagain:
        player = player_choice()
        computer = computer_choice()
        print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
        print("\nPython chose " + str(RPS(computer)).replace('RPS.', '')+".\n")
        result = winner(player,computer)
        print(result)
        playagain = input("\nPlay again? \nY for yes or \nQ to quit\n\n").lower()
        if playagain != "y":
            playagain = False
    print("\n🎉🎉🎉")
    print("Thank you for playing!\n")

if __name__ == "__main__":
    main()