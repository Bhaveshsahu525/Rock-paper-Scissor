# Rock paper scissor

import random

user_wins = 0
computer_wins = 0
tie = 0
options = ["r", "p", "s"]

while True:
    user_pick = input(f"Please choose 'r' for rock 's' for scissor 'p' for paper Or Press Q to quit: ").lower()
    if user_pick == "q":
        print("You quit.")
        print(f"You won {user_wins} times and computer wins {computer_wins} times and got tied {tie} times")
        break
    elif user_pick not in options:
        print("Please enter a valid input.")
        continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("The computer picked", computer_pick)
    if (computer_pick == "r" and user_pick == "s") or (computer_pick == "p" and user_pick == "r") or (computer_pick == "s" and user_pick == "p"):
        print("You lost!")
        computer_wins += 1

    elif computer_pick == user_pick:
        print("tie")
        tie += 1

    else:
        print('You win!')
        user_wins += 1
