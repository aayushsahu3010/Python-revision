import random

# Take input
user_choice = int(input("!! What do you choose in rock paper scissor? Type 0 for Rock, 1 for Paper, 2 for Scissors !! "))

# Check invalid input
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose.")
else:
    # Computer choice
    computer_choice = random.randint(0, 2)

    game_images = ["Rock", "Paper", "Scissors"]

    print(f"\nYou chose: {game_images[user_choice]}")
    print(f"Computer chose: {game_images[computer_choice]}")

    # Game logic
    if user_choice == computer_choice:
        print("It's a draw.")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose.")
