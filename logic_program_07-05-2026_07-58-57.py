```python
import random # This line imports the 'random' module, which contains functions for generating random numbers and choices.

# This function takes a string (a word) and returns a new string with its letters shuffled.
def create_random_word_jumble(original_word):
    # Convert the input word string into a list of its individual characters.
    # Strings are immutable in Python, but lists are mutable (can be changed).
    list_of_chars = list(original_word)
    
    # Use random.shuffle to randomly reorder the elements (characters) in the list.
    # This operation modifies the list 'list_of_chars' directly.
    random.shuffle(list_of_chars)
    
    # Join the shuffled characters back together to form a new string.
    # The "" before .join() means there's no separator between the joined characters.
    jumbled_word = "".join(list_of_chars)
    
    return jumbled_word # Return the newly created jumbled word.

# Prompt the user to enter a word they want to jumble.
# The input() function gets text from the user.
user_input_word = input("Enter a word to create a jumble from: ")

# Call our function to get the jumbled version of the user's word.
jumbled_version = create_random_word_jumble(user_input_word)

# Print both the original word and its jumbled version.
# f-strings (formatted string literals) are a modern way to embed expressions inside string literals.
print(f"Your original word: {user_input_word}")
print(f"Your jumbled word: {jumbled_version}")

```
