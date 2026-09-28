import random

programms_number = random.randint(1, 100)

while True:
    try:
        users_number = int(input("Guess the number between 1 and 100:"))

        if users_number > programms_number:
            print("Too high!")
        elif users_number < programms_number:
            print("Too low!")
        else:
            print("Congratulations!\n You found the number!")
            break

    except ValueError:
        print("Please enter a valid number")
