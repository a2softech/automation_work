```python
# This script helps you generate a unique, simple nickname based on your favorite animal and a lucky number!

import random # We need this module to pick a random name suffix

# Define a list of common, friendly animal names
animals = ["dog", "cat", "bird", "fish", "rabbit", "hamster", "turtle", "snake", "mouse"]

# Define a list of silly or cool suffixes for the nickname
suffixes = ["Master", "King", "Queen", "Noodle", "Paws", "Whiskers", "Snout", "Tail", "Fangs", "Wings", "Fins"]

# Get the user's favorite animal as input
# We convert it to lowercase to make matching easier later
favorite_animal = input("What's your favorite animal? ").lower()

# Get a lucky number from the user
# We convert the input to an integer because input() always returns a string
try:
    lucky_number = int(input("What's your lucky number (a whole number)? "))
except ValueError:
    # Handle cases where the user doesn't enter a valid number
    print("That wasn't a valid number! Using 7 as your lucky number instead.")
    lucky_number = 7

# Now, let's create the nickname!

# First, let's make sure the favorite animal is in our list.
# If not, we'll pick a random one from our list.
if favorite_animal not in animals:
    print(f"'{favorite_animal}' isn't in my list! Picking a random animal for you...")
    chosen_animal = random.choice(animals) # Pick a random animal from our 'animals' list
else:
    chosen_animal = favorite_animal # Use the user's favorite animal

# Choose a random suffix from our 'suffixes' list
chosen_suffix = random.choice(suffixes)

# Combine them to form the unique nickname
# We also incorporate the lucky number to make it even more unique
nickname = f"{chosen_animal.capitalize()}{chosen_suffix}{lucky_number}"

# Print out the generated nickname
print(f"\nYour unique nickname is: {nickname}!")
print("Hope you like it!")
```
