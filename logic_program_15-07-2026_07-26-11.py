# Import the 'random' module to use its shuffling capabilities.
import random

# Greet the user and explain the purpose of the script.
print("Welcome to the Secret Word Mixer!")
print("I'll take any word you give me and mix up its letters.")

# Ask the user to input a word.
# The input() function reads text from the console.
user_word = input("Please enter a word (letters only, no spaces): ")

# Convert the input word into a list of its individual characters.
# For example, "python" becomes ['p', 'y', 't', 'h', 'o', 'n'].
word_characters = list(user_word)

# Randomly shuffle (rearrange) the order of characters in the list.
# This changes the list in place, so 'word_characters' is now shuffled.
random.shuffle(word_characters)

# Join the shuffled characters back together to form a new string.
# The "".join() method concatenates strings from an iterable (like our list)
# with an empty string "" as the separator.
mixed_word = "".join(word_characters)

# Print the original and the newly mixed word for the user.
print("\nYour original word was:", user_word)
print("Here's your mixed-up word:", mixed_word)

# Encourage the user with a final message.
print("Can you still recognize it?")
