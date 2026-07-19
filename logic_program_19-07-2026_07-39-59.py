```python
# This script creates a "secret" version of your word
# by placing a special character between each letter.

# 1. Get a word from the user.
original_word = input("Enter a word to make secret: ")

# 2. Get a single character from the user to use as a separator.
separator_char = input("Enter a single character to separate (e.g., '-', '*', '#'): ")

# 3. Create an empty string to build our secret message.
secret_version = ""

# 4. Loop through each letter in the original word.
# 'range(len(original_word))' gives us numbers from 0 up to (length - 1).
for index in range(len(original_word)):
    # Get the current letter using its index.
    current_letter = original_word[index]

    # Add the current letter to our secret message.
    secret_version += current_letter

    # Check if it's NOT the last letter in the word.
    # We don't want to add a separator after the very last letter.
    if index < len(original_word) - 1:
        # If it's not the last letter, add the separator character.
        secret_version += separator_char

# 5. Print the final secret version of the word.
print("\nYour secret word is:")
print(secret_version)
```
