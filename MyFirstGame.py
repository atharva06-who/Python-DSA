import random 
user_choice = int(input("What do you choose? Type 0 for rock or Type 1 for Paper or Type 2 for Scissors\n"))
computer_choice = random.randint(0,2)
print(f"computer chose: {computer_choice}")
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("It's a draw!")
