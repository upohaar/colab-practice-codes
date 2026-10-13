# Storing data in variables
x = 10
y = 5
name = "Alice"

# Basic arithmetic
total = x + y

# Printing variables (using an 'f-string' to mix text and variables)
print(f"Hi {name}, the total of {x} + {y} is {total}.")


# input() always captures text as a String
user_name = input("What is your name? ")
print(f"Great to meet you, {user_name}!")

# To get a number, you must convert it using int() or float()
age_input = input("How old are you? ")
age = int(age_input)  # Converts the text to an integer (whole number)
print(f"Next year, you will be {age + 1} years old.")




score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C or below")

    # Defining a function with 'def'
def greet_user(username):
    print(f"Hello, {username}! Have a fantastic day.")

# Calling the function
greet_user("Bob")
greet_user("Charlie")


# This is a comment. Python ignores lines starting with '#'
print("Hello, World!")
print("Welcome to Python programming!")

import random

secret_number = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10.")

guess = int(input("Take a guess: "))

if guess == secret_number:
    print("Correct! You win!")
else:
    print(f"Wrong! The number was {secret_number}.")


import random

choices = ["rock", "paper", "scissors"]

print("--- Rock, Paper, Scissors ---")
user_choice = input("Enter rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
elif user_choice in choices:
    print("Computer wins!")
else:
    print("Invalid choice! Please restart and type rock, paper, or scissors.")


import random
import time

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


    import csv
from datetime import datetime

class Expense:
    def __init__(self, amount, category, description):
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        # Ensure file exists and has a header
        try:
            with open(self.filename, 'x', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Amount", "Category", "Description"])
        except FileExistsError:
            pass

    def add_expense(self, expense):
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([expense.date, expense.amount, expense.category, expense.description])
        print("Expense recorded successfully!")

    def get_summary(self):
        total = 0.0
        categories = {}
        try:
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    amt = float(row["Amount"])
                    total += amt
                    categories[row["Category"]] = categories.get(row["Category"], 0.0) + amt
            
            print(f"\n--- Total Expenses: ${total:.2f} ---")
            for cat, amt in categories.items():
                print(f" * {cat}: ${amt:.2f}")
        except FileNotFoundError:
            print("No expenses recorded yet.")

# Example Usage
if __name__ == "__main__":
    tracker = ExpenseTracker()
    
    # Simulating adding data
    tracker.add_expense(Expense(12.50, "Food", "Lunch at cafe"))
    tracker.add_expense(Expense(45.00, "Transport", "Gas fill up"))
    tracker.add_expense(Expense(8.99, "Food", "Coffee snack"))
    
    # Generate aggregate metrics
    tracker.get_summary()


    import requests
import time
import sys

def fetch_crypto_prices(crypto_ids=["bitcoin", "ethereum", "solana"]):
    """Fetches real-time price trends using the CoinGecko public API."""
    url = "https://coingecko.com"
    params = {
        "ids": ",".join(crypto_ids),
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Raise exception for bad HTTP status
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"\nError contacting API: {e}")
        return None

def display_dashboard():
    print("Fetching live market tracking data (Press Ctrl+C to exit)...")
    try:
        while True:
            data = fetch_crypto_prices()
            if data:
                # Clear terminal line tricks or print dividers
                print(f"\n--- Market Update: {time.strftime('%H:%M:%S')} ---")
                for coin, details in data.items():
                    price = details.get("usd", 0)
                    change = details.get("usd_24h_change", 0)
                    sign = "+" if change >= 0 else ""
                    print(f"{coin.capitalize():<12}: ${price:,.2f} ({sign}{change:.2f}%)")
            
            # Throttle requests to respect public API rate limits
            time.sleep(15)
    except KeyboardInterrupt:
        print("\nDashboard closed safely.")
        sys.exit()

if __name__ == "__main__":
    display_dashboard()