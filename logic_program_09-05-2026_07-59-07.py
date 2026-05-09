```python
# A unique, short Python script for beginners: The Echo Word Chopper!

# This script takes a word and 'chops' off characters from the end,
# printing it multiple times, getting shorter each time.

# First, we ask the user to input a word.
# The input() function gets text from the user.
# The text inside input() is a prompt that the user will see.
user_word = input("Enter a word (e.g., 'keyboard'): ")

# Print a header to make the output clear.
print("\n--- Echo Chopper Output ---")

# We use a 'for' loop to iterate through the word.
# 'range(len(user_word))' generates numbers from 0 up to (length of word - 1).
# 'i' will represent the number of characters to keep from the start of the word.
for i in range(len(user_word)):
    # Slice the word: 'user_word[:i+1]' means "start from the beginning (0)
    # and go up to, but not including, index i+1".
    # This effectively gets the first 1, then 2, then 3 characters, and so on.
    chopped_word = user_word[:i+1]

    # Print the progressively longer 'chopped' word.
    print(chopped_word)

# Print a final message.
print("--------------------------")
print("Echo Chopper finished!")
```
