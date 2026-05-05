```python
# This script creates a simple "Word Scrambler" game.

# First, we need to import the 'random' module.
# The 'random' module provides functions for generating random numbers and choices,
# which we'll use to shuffle the letters of a word.
import random

# Ask the user to input a word.
# The 'input()' function displays a message and waits for the user to type something,
# then returns the typed text as a string.
user_word = input("Enter a word to scramble: ")

# Convert the input word (which is a string) into a list of characters.
# Strings in Python are 'immutable' (cannot be changed after creation),
# but lists are 'mutable' (their elements can be changed, added, or removed).
# We convert it to a list so we can shuffle its characters.
word_as_list = list(user_word)

# Use the 'random.shuffle()' function to randomly reorder the elements
# (which are individual characters in this case) within the 'word_as_list'.
# This function shuffles the list 'in-place', meaning it modifies the list directly.
random.shuffle(word_as_list)

# Join the shuffled characters back together to form a single scrambled word string.
# The "" at the beginning means "join the list elements with an empty string as a separator".
# So, ['h', 'e', 'l', 'l', 'o'] might become "hlelo".
scrambled_word = "".join(word_as_list)

# Display the original word and its scrambled version to the user.
# We're using an f-string (formatted string literal) for easy output formatting.
print(f"\nYour original word was: {user_word}")
print(f"Your scrambled word is: {scrambled_word}")

# You can try to unscramble it yourself!
```
