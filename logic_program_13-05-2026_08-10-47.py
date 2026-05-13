```python
# This simple script generates a unique "fortune" based on your favorite number!

# First, we ask the user for their favorite number.
# The input() function gets text from the user.
# int() converts that text into a whole number (integer).
try:
    favorite_number = int(input("Enter your favorite whole number (e.g., 7, 42): "))
except ValueError:
    # If the user doesn't enter a valid number, we set a default.
    print("That wasn't a valid number! Using 13 as default.")
    favorite_number = 13

# Next, we ask for a short, happy word.
happy_word = input("Enter a short, happy word (e.g., 'joy', 'smile'): ")

# We'll make sure the happy word is in lowercase for consistency.
happy_word = happy_word.lower()

# Now, let's create a unique "fortune" based on the inputs!

# The "magic" phrase starts with a repetitive pattern from the number.
# We use string multiplication to repeat a character.
# The modulo operator (%) gives the remainder of a division.
# This helps create a varying pattern based on the number.
magic_pattern = ("*" * (favorite_number % 5 + 1)) + " "

# The core of the fortune will be the happy word repeated.
# We use max(1, ...) to ensure the word is repeated at least once,
# even if favorite_number is 0 or negative.
fortune_core = (happy_word + " ") * max(1, (favorite_number // 3) % 4)

# We use an f-string (formatted string literal) to easily combine text and variables.
# This is a modern and clean way to build strings.
your_fortune = (
    f"\n{magic_pattern}Your custom fortune is: {fortune_core.strip()}{magic_pattern}\n"
    f"Remember, {happy_word.capitalize()} brings great things to {favorite_number} lucky people!"
)

# Finally, we print the generated fortune!
print(your_fortune)

# Try running it multiple times with different numbers and words to see the variations!
```
