```python
# This script creates a personalized "magic box" using a character and size you choose!

# --- 1. Get user input for the box ---
# Ask the user for a single character to draw the box with.
# The `input()` function reads what the user types into the console.
box_character = input("Enter a single character to build your magic box (e.g., #): ")

# Ask the user for the size of the box.
# We convert the input (which is text) into a whole number using `int()`.
# This number will determine how wide and tall the box is.
box_size_str = input("Enter a size for your box (a number like 5 or 7): ")
box_size = int(box_size_str)

# --- 2. Draw the top border of the box ---
# The top border is a line of `box_character` repeated `box_size` times.
# String multiplication (e.g., '*' * 5) repeats the string.
print(box_character * box_size)

# --- 3. Draw the middle section of the box ---
# We loop `box_size - 2` times to draw the middle rows.
# '- 2' is because the top and bottom borders are already drawn.
for _ in range(box_size - 2):
    # Each middle row starts with the `box_character`.
    # Then it has `box_size - 2` spaces for the empty inside of the box.
    # Finally, it ends with another `box_character`.
    # ' ' * (box_size - 2) creates the empty space in the middle.
    print(box_character + " " * (box_size - 2) + box_character)

# --- 4. Draw the bottom border of the box ---
# The bottom border is identical to the top border.
print(box_character * box_size)

# A friendly message to tell the user the script has finished.
print("\nYour magic box is complete!")
```
