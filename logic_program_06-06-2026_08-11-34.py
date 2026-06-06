```python
# This script takes a word from the user and prints a unique 'wave' pattern.
# It showcases basic input, string manipulation, and loop concepts for beginners.

# 1. Get user input:
# The 'input()' function displays a message and waits for the user to type something,
# then returns that text as a string.
user_word = input("Enter a word: ")

# 2. Basic input validation:
# Check if the user actually entered a word. An empty string is 'falsy'.
if not user_word:
    print("You didn't enter a word. Exiting.")
else:
    # 3. Process the word:
    # Convert the word to lowercase to handle different capitalizations consistently.
    # This is a good practice for string comparisons or patterns.
    user_word = user_word.lower()
    
    # Store the length of the word for easier use in loops.
    word_length = len(user_word)

    # 4. Print the "growing" part of the wave:
    # This loop iterates from 0 up to (but not including) word_length.
    # In each iteration, it prints a slice of the word, starting from the beginning
    # and getting progressively longer.
    # Example for 'hello': 'h', 'he', 'hel', 'hell', 'hello'
    for i in range(word_length):
        # String slicing user_word[:i+1] means:
        # Start from the beginning (index 0) up to index 'i+1' (exclusive).
        # When i=0, it prints user_word[0:1] which is the first letter.
        # When i=word_length-1, it prints user_word[0:word_length] which is the whole word.
        print(" " * i + user_word[:i+1]) # Add leading spaces to create a diagonal effect

    # 5. Print the "shrinking" part of the wave:
    # This loop iterates backward, from word_length-2 down to -1 (exclusive of -1).
    # This creates the second half of the wave, ensuring the full word is not repeated
    # immediately before shrinking.
    # Example for 'hello': 'hell', 'hel', 'he', 'h' (indented further)
    for i in range(word_length - 2, -1, -1):
        # Again, string slicing for the word part.
        # The number of leading spaces increases as the word shrinks, continuing the diagonal.
        print(" " * (i + word_length) + user_word[:i+1])

    # 6. Final message (optional but good for beginner scripts)
    print("\nPattern complete!")
```
