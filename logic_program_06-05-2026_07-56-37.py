```python
# A simple, interactive 'Dice Roller' simulator!
# This script lets you 'roll' a virtual six-sided die and shows the result.

import random # The 'random' module helps us generate random numbers.

print("Welcome to the Simple Dice Roller!")
print("Type 'roll' to roll the die, or 'quit' to exit.")

# Start an infinite loop that will keep running until the user decides to quit.
while True:
    # Get input from the user. We convert it to lowercase for easier comparison.
    user_input = input("\nReady to roll? (Type 'roll' or 'quit'): ").lower()

    if user_input == 'quit':
        # If the user types 'quit', we break out of the loop.
        print("\nThanks for rolling! Goodbye!")
        break # This statement exits the 'while' loop.
    elif user_input == 'roll':
        # If the user types 'roll', we simulate a die roll.

        # random.randint(1, 6) generates a random integer between 1 and 6 (inclusive).
        roll_result = random.randint(1, 6)

        # Print the result using an f-string, a modern way to format strings.
        print(f"You rolled a: {roll_result}!")
    else:
        # If the user types something other than 'roll' or 'quit'.
        print("Invalid input. Please type 'roll' or 'quit'.")
```
