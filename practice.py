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