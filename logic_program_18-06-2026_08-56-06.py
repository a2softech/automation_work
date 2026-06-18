```python
# Ask the user for a small number to control the pattern's size
pattern_size_str = input("Enter a small positive integer (e.g., 3-7): ")

# Try to convert the user's input into an integer
# If the input isn't a valid number, we'll set a default size
try:
    pattern_size = int(pattern_size_str)
except ValueError:
    print("That wasn't a number! Defaulting pattern size to 5.")
    pattern_size = 5 # Default value if conversion fails

# Ensure the pattern size is positive and within a reasonable range
if pattern_size <= 0 or pattern_size > 10:
    print("Size must be between 1 and 10. Defaulting to 4.")
    pattern_size = 4 # Default if input is out of range

# Define the characters we'll use to draw our unique pattern
char1 = ">"
char2 = "<"
char3 = "="
char4 = "*"
empty_space = " "

# Print a simple header for the pattern
print("\n--- Your Unique Echo Pattern ---")

# Loop to generate different lines of the pattern
# The loop runs 'pattern_size' times for the first half, then again for the second
for i in range(pattern_size * 2 - 1):
    # Determine the current length of the pattern section based on 'i'
    if i < pattern_size:
        # For the first half, the pattern grows
        current_length = i + 1
    else:
        # For the second half, the pattern shrinks back down
        current_length = pattern_size * 2 - 1 - i

    # Calculate the number of leading spaces needed to center the pattern
    # This makes the pattern appear centered rather than left-aligned
    leading_spaces = (pattern_size - current_length) * 2

    # Build the line using string multiplication and concatenation
    # String multiplication repeats a character a specified number of times
    line = (empty_space * leading_spaces) + \
           (char1 * current_length) + \
           (char3 * (pattern_size - current_length)) + \
           (char2 * current_length) + \
           (char4 * current_length) # Adding a final character section

    # Print the constructed line
    print(line)

# Print a concluding message
print("--- Pattern Generation Complete! ---\n")
```
