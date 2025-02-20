import random

options = ["paper", "scissors", "rock"]

def user_choice(): #Chiede all'utente di scegliere un'opzione  
    choice = input("Choose your option: ")
    if choice in options:
        return choice
    else:
        print("Invalid choice")
        return user_choice()

def computer_choice():
    return random.choice(options) #Genera casualmente una scelta per il computer

def tie_condition(user, computer):
    if user == computer:
        return "It's a tie! (˶°ㅁ°)!!"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "You won! ദ്ദി •⩊• )"
    else:
        return "You lose! (っ- ‸ - ς)"

user = user_choice()
computer = computer_choice()
print(f"User choice: {user}")
print(f"Computer choice: {computer}")
result = tie_condition(user, computer)
print(result)
