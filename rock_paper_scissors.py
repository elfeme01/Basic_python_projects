import random

choices = ("r", "p", "s")
emojis = {"r": "🪨", "p": "📃", "s": "✂️"}

while True:

    user_choice = input("Rock, paper of scissors? (r/p/s):").lower()
    if user_choice not in choices:
        print('Invalid choice!')
        continue

    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "p" and computer_choice == "r") or
            (user_choice == "p" and computer_choice == "r")):
        print("YOU WIN")
    elif user_choice == computer_choice:
        print("it's a tie")
    else:
        print("You lost!")

    should_continue = input("Continue? (y/n):").lower()
    if should_continue == "n":
        break
