import random

c = 0  # Computer score
u = 0  # User score

user = input("Enter (R for Rock)(P for Paper)(S for Scissors)(Q for Quit): ")

while user.lower() != "q":
    computer = random.randrange(0, 3)  # (0 for Rock)(1 for Paper)(2 for Scissors)

    # Map user input to string
    if user.lower() == "r":
        user_choice = "Rock"
    elif user.lower() == "p":
        user_choice = "Paper"
    elif user.lower() == "s":
        user_choice = "Scissors"
    else:
        print("Invalid input!")
        user = input("Enter (R for Rock)(P for Paper)(S for Scissors)(Q for Quit): ")
        continue

    # Map computer input to string
    if computer == 0:
        computer_choice = "Rock"
    elif computer == 1:
        computer_choice = "Paper"
    elif computer == 2:
        computer_choice = "Scissors"

    print(f"You choose: {user_choice}")
    print(f"Computer choose: {computer_choice}")

    # Draw
    if (computer_choice==user_choice):
        print("It is a draw!")

    # Computer win
    elif (computer_choice == "Rock" and user_choice == "Scissors") or \
         (computer_choice == "Paper" and user_choice == "Rock") or \
         (computer_choice == "Scissors" and user_choice == "Paper"):
        print("Computer won this time!")
        c += 1

    # User win
    else:
        print("You won this time!")
        u += 1

    user = input("\nEnter (R for Rock)(P for Paper)(S for Scissors)(Q for Quit): ")

print(f"\nYour score: {u}\nComputer score: {c}")
