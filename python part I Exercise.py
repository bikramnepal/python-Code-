#!/usr/bin/env python
# coding: utf-8

# # Exercise-2
# ## Date: 7th Feb 2024
# # submitted to : Melinda Varo
# # submitted by: Bikram Nepal

# # 1

# In[1]:


# Define two variables and assign them values
num1 = 100
num2 = 29

# Sum up the two numbers and multiply the result by 3
result = (num1 + num2) * 3

# Calculate the 2nd exponent of the previous result and save it to a new variable
exponent_result = result ** 2

# Print the final result
print("The result is:", exponent_result)


# # 2

# In[2]:


# Ask user for their name, year of birth, and age
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
age = int(input("Enter your age: "))
# Extract last two digits of the year of birth
last_two_digits_year = str(year_of_birth)[-2:]
# Take the first three letters of the name
first_three_letters_name = name[:3]
# Calculate the second power of the age
age_power_2 = age ** 2
# Construct the password
password = last_two_digits_year + first_three_letters_name + str(age_power_2)
# Print the password
print("Password:", password)


# # 3

# In[9]:


# Ask user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Check if both numbers are even
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
# Check if only one of the numbers is even
elif num1 % 2 == 0 or num2 % 2 == 0:
    print("One of the numbers is even.")
# If neither of the numbers is even
else:
    print("Both numbers are odd.")


# In[4]:


# Ask user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Check if both numbers are even
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
# Check if only one of the numbers is even
elif num1 % 2 == 0 or num2 % 2 == 0:
    print("One of the numbers is even.")
# If neither of the numbers is even
else:
    print("Both numbers are odd.")


# In[5]:


# Ask user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Check if both numbers are even
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
# Check if only one of the numbers is even
elif num1 % 2 == 0 or num2 % 2 == 0:
    print("One of the numbers is even.")
# If neither of the numbers is even
else:
    print("Both numbers are odd.")


# # 4

# In[6]:


# Ask the user for an integer
number = int(input("Give an integer: "))
# Initialize the sum
total_sum = 0
# Iterate from 0 to the user given input (exclusive) and calculate the sum of positive numbers
for i in range(number):
    total_sum += i
# Print the result
print("The sum of numbers upto:",number, "=" ,total_sum)


# # 5

# In[7]:


import random
# Generate a random number between 0 and 10
target_number = random.randint(0, 10)
# Initialize number of tries
tries = 0
# Start the guessing game
while True:
    # Ask the player for a guess
    guess = int(input("Player: "))
    # Increment the number of tries
    tries += 1
    # Check if the guess is correct
    if guess == target_number:
        print("That’s right! Number of tries:", tries)
        break
    elif guess < target_number:
        print("Try a greater number.")
    else:
        print("Try a smaller number.")


# # Bonus

# In[8]:


import random
def play_game(player_name):
    # Generate a random number between 0 and 10
    target_number = random.randint(0, 10)
    # Initialize number of tries
    tries = 0
    # Start the guessing game
    while True:
        # Ask the player for a guess
        guess = int(input(f"{player_name}: "))
        # Increment the number of tries
        tries += 1
        # Check if the guess is correct
        if guess == target_number:
            print(f"That’s right, {player_name}! Number of tries:", tries)
            return tries
        elif guess < target_number:
            print("Try a greater number.")
        else:
            print("Try a smaller number.")
# Play the game for Player 1
print("Player 1's turn:")
player1_tries = play_game("Player 1")
# Play the game for Player 2
print("Player 2's turn:")
player2_tries = play_game("Player 2")
# Compare the number of tries and determine the winner
if player1_tries < player2_tries:
    print("Player 1 wins!")
elif player2_tries < player1_tries:
    print("Player 2 wins!")
else:
    print("It's a tie!")

