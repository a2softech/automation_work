```python
# This script takes a word from you and creates a fun, silly version of it!

# Ask the user to type in any word they like
original_word = input("Type a word (e.g., 'Python', 'banana'): ")

# Convert the entire word to lowercase for consistent processing
word_lower = original_word.lower()

# Take the first character of the word
first_char = word_lower[0]

# Take the rest of the word, starting from the second character
rest_of_word = word_lower[1:]

# Define a fun, fixed ending for our silly word
silly_suffix = "aloo"

# Combine the parts: capitalize the first char, add the rest, then add the suffix
silly_word = first_char.upper() + rest_of_word + silly_suffix

# Print out the original word and its new silly transformation
print(f"\nYour original word: '{original_word}'")
print(f"Your silly word is: '{silly_word}'!")
```
