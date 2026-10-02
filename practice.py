# # Storing data in variables
# x = 10
# y = 5
# name = "Alice"

# # Basic arithmetic
# total = x + y



# # Printing variables (using an 'f-string' to mix text and variables)
# print(f"Hi {name}, the total of {x} + {y} is {total}.")


# # input() always captures text as a String
# user_name = input("What is your name? ")
# print(f"Great to meet you, {user_name}!")

# # To get a number, you must convert it using int() or float()
# age_input = input("How old are you? ")
# age = int(age_input)  # Converts the text to an integer (whole number)
# print(f"Next year, you will be {age + 1} years old.")

# score = 85

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# else:
#     print("Grade: C or below")

#     # Defining a function with 'def'
# def greet_user(username):
#     print(f"Hello, {username}! Have a fantastic day.")

# # Calling the function
# greet_user("Bob")
# greet_user("Charlie")


# # This is a comment. Python ignores lines starting with '#'
# print("Hello, World!")
# print("Welcome to Python programming!")

# import random

# secret_number = random.randint(1, 10)
# print("I'm thinking of a number between 1 and 10.")

# guess = int(input("Take a guess: "))

# if guess == secret_number:
#     print("Correct! You win!")
# else:
#     print(f"Wrong! The number was {secret_number}.")


# import random

# choices = ["rock", "paper", "scissors"]

# print("--- Rock, Paper, Scissors ---")
# user_choice = input("Enter rock, paper, or scissors: ").lower()
# computer_choice = random.choice(choices)

# print(f"Computer chose: {computer_choice}")

# if user_choice == computer_choice:
#     print("It's a tie!")
# elif (user_choice == "rock" and computer_choice == "scissors") or \
#      (user_choice == "paper" and computer_choice == "rock") or \
#      (user_choice == "scissors" and computer_choice == "paper"):
#     print("You win!")
# elif user_choice in choices:
#     print("Computer wins!")
# else:
#     print("Invalid choice! Please restart and type rock, paper, or scissors.")


# import random
# import time

print("--- Dice Roller Battle ---")

playing = True
while playing:
    input("Press Enter to roll the dice...")
    
    user_roll = random.randint(1, 6)
    comp_roll = random.randint(1, 6)
    
    print(f"You rolled: {user_roll}")
    print("Computer is rolling...")
    time.sleep(1) # Adds a 1-second dramatic pause
    print(f"Computer rolled: {comp_roll}")
    
    if user_roll > comp_roll:
        print("You win this round!")
    elif comp_roll > user_roll:
        print("Computer wins this round!")
    else:
        print("It's a draw!")
        
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        playing = False

print("Thanks for playing!")




print("--- Haunted Castle Adventure ---")
print("You stand in front of a dark castle. The grand door is open.")

choice1 = input("Do you enter through the 'door' or look for a 'window'? ").lower()

if choice1 == "door":
    print("\nYou walk into the dark hallway. A giant vampire appears!")
    choice2 = input("Do you 'fight' or 'run'? ").lower()
    
    if choice2 == "run":
        print("\nYou safely escape out the door. You live to see another day! (Good Ending)")
    else:
        print("\nYou tried to fight a vampire with no weapons? Game Over! (Bad Ending)")

elif choice1 == "window":
    print("\nYou climb through the window and land directly inside the treasure room!")
    choice2 = input("Do you 'take' the gold or 'leave' it alone? ").lower()

    
    if choice2 == "take":
        print("\nTaking the gold triggers a trap! The room fills with water. Game Over! (Bad Ending)")
    else:
        print("\nYou leave the gold, find a safe secret exit, and escape unharmed! (Safe Ending)")

else:
    print("\nYou hesitated too long and a ghost scared you away! Game Over.")