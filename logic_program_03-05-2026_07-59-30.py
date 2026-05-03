```python
# This script takes a word and a special character, then makes each letter "streak"!

import random # We'll use this to make the streak lengths a little varied and fun.

# Ask the user for any word they want to see "streaked"
user_word = input("Enter a word: ")

# Ask the user for the single character they want to use for the streaks
streak_char = input("Now, enter ONE character to make the streak (e.g., '-', '=', '*'): ")

# A small check to make sure the user entered only one character for the streak
if len(streak_char) != 1:
    print(f"\nOops! You entered '{streak_char}'. No worries, we'll use '-' for the streaks instead.")
    streak_char = "-" # If input is bad, we set a default to keep the script running

print("\n--- Get ready for your streaky word! ---")

# Now, we go through each letter in the user's word, one by one
# The 'for' loop is perfect for repeating actions for each item in a sequence.
for letter in user_word:
    # We convert each letter to uppercase to make it stand out more
    upper_letter = letter.upper()

    # Decide how long this letter's streak should be
    # 'random.randint(3, 8)' will pick a whole number between 3 and 8 (inclusive)
    streak_length = random.randint(3, 8)

    # Create the actual streak part by multiplying the 'streak_char'
    # This is a neat trick: 'character * number' repeats the character that many times
    current_streak = streak_char * streak_length

    # Combine the uppercase letter with its streak
    # The '+' sign here joins strings together
    streaked_line = upper_letter + current_streak

    # Print the complete streaked line for this letter
    print(streaked_line)

print("\n--- Done streaking! Hope you enjoyed it! ---")
```
