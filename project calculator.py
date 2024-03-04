#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Calling math library square root function

from math import sqrt   

# Defining the needed functions to run the calculator program

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"   # Adding error message
    else:
        return x / y
def power(x):
    return x ** 2
def square_root(x):
    if x < 0:
        return "Cannot calculate square root of a negative number!"  # Adding error message
    else:
        return sqrt(x)

# User Menu 

def print_menu():
    print("  ")  # Space for better visibility
    print("Menu:")
    print("  1. Addition")
    print("  2. Subtraction")
    print("  3. Multiplication")
    print("  4. Division")
    print("  5. Second Power")
    print("  6. Square Root")
    print("  7. Exit")
    print("  ")  # Space for better visibility
    
def user_input():  # Function selection with validation
    valid_choices = (1, 2, 3, 4, 5, 6, 7)
    while True:
        try:
            choice = int(input("Enter Function Number: "))
            if choice in valid_choices:
                return choice
            else:
                print("Please enter a valid choice from (1, 2, 3, 4, 5, 6, 7).") # validation in case of Integer selection
        except ValueError:
            print("Please enter a valid choice from (1, 2, 3, 4, 5, 6, 7).") # validation in case of other selections

def get_number(message):
    while True:
        try:
            return float(input(message))  # Prompt for a number
        except ValueError:
            print("Please enter a valid number.") # validation in case of Worng input

while True:    # To choose the desired operation over and over again until the user chooses to quit using it. 
    print_menu()
    choice = user_input()

    if choice == 7:  # To break the loop and close the program 
        print("Shutdown...")
        break

    # Calling the pre-defined function to perform the calculation according to the user selection
    if choice == 6:
        x = get_number("Enter the number: ")
        result = square_root(x)
    elif choice == 5:
        x = get_number("Enter the number: ")
        result = power(x)
    else:
        x = get_number("Enter first number: ")
        y = get_number("Enter second number: ")
        if choice == 1:
            result = add(x, y)
        elif choice == 2:
            result = subtract(x, y)
        elif choice == 3:
            result = multiply(x, y)
        elif choice == 4:
            result = divide(x, y)
            
    print("  ")  # Space for better visibility
    print("Result:", result)
    print("  ")  # Space for better visibility

