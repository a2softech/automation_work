```python
# Ask the user for a short word to play with
user_word = input("Enter a short word (e.g., 'Python'): ")

# If the user didn't enter anything, use a default word
if not user_word:
    user_word = "CODE"

# Convert the word to uppercase for consistent display
user_word = user_word.upper()

# Get the length of the word
word_length = len(user_word)

print("\n--- Word Magic! ---")

# Part 1: Make the word grow letter by letter
print("\nGrowing:")
# Loop from 0 up to (but not including) the word's length
for i in range(word_length):
    # Print a slice of the word, starting from the beginning
    # and extending one more letter with each loop iteration
    print(user_word[0 : i + 1])

# Part 2: Make the word shrink letter by letter
print("\nShrinking:")
# Loop from the word's length down to 1 (not including 0)
for i in range(word_length, 0, -1):
    # Print a slice of the word, starting from the beginning
    # and shortening one letter with each loop iteration
    print(user_word[0 : i])

print("\n--- Magic Complete! ---")
```
