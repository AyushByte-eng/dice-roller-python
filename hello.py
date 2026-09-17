 import random

while True:
    choice = input("Roll the dice? (yes/no): ").lower()

    if choice == "yes":
        dice = random.randint(1, 6)
        print("🎲 You rolled:", dice)

    elif choice == "no":
        print("Thanks for playing! 👋")
        break

    else:
        print("Please enter yes or no.")
