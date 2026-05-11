```python
# This script creates a simple "text art" pattern based on user input.

# Ask the user to type in a word or a short phrase.
# The 'input()' function waits for the user to type something and press Enter.
user_word = input("Enter a word or a short phrase: ")

# Get the length (number of characters) of the user's input.
# The 'len()' function returns the length of a string.
word_length = len(user_word)

# Print a header to make the output clear.
print("\n--- Your Pattern ---")

# Use a 'for' loop to repeat a block of code multiple times.
# 'range(1, word_length + 1)' generates numbers from 1 up to 'word_length'.
# For example, if user_word is "CAT" (length 3), 'i' will be 1, then 2, then 3.
for i in range(1, word_length + 1):
    # Print the user's word, repeated 'i' times.
    # Python allows multiplying a string by an integer to repeat it.
    # Example: "CAT" * 1 -> "CAT"
    # "CAT" * 2 -> "CATCAT"
    # "CAT" * 3 -> "CATCATCAT"
    print(user_word * i)

# Print a footer to indicate the end of the pattern.
print("--------------------")
```
