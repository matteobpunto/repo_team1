import random

options = ["paper", "scissors", "rock"]

def user_choice():
    choice = input("Choose your option: ")
    if choice in options:
        return choice
    else:
        print("Invalid choice. Please choose paper, scissors, or rock.")
        return user_choice()

def computer_choice():
    return random.choice(options)

def tie_condition(user, computer):
    if user == computer:
        return "Tie!"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "You won!"
    else:
        return "You've lost!"

user = user_choice()
computer = computer_choice()
print(f"User choice: {user}")
print(f"Computer choice: {computer}")
result = tie_condition(user, computer)
print(result)
