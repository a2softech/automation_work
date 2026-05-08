```python
# This script creates a tiny, personalized 'lucky number' based on your name.

# Welcome the user and ask for their name.
name = input("Hello there! What's your first name? ").strip()

# Check if the name is empty. If so, provide a default name.
if not name:
    name = "Mysterious Friend"
    print("No name? No problem! We'll call you Mysterious Friend.")

# Convert the name to lowercase for consistent processing.
name_lower = name.lower()

# Calculate a 'lucky number' by summing the ASCII values of the letters.
# We'll use a simple loop for this.
lucky_number_sum = 0
for char in name_lower:
    if 'a' <= char <= 'z': # Only consider alphabetic characters
        # Convert character to a number (a=1, b=2, ..., z=26)
        # ord('a') gives the ASCII value of 'a'.
        lucky_number_sum += (ord(char) - ord('a') + 1)

# If the sum is zero (e.g., if the name only had spaces or non-letters),
# assign a default lucky number to avoid confusion.
if lucky_number_sum == 0:
    lucky_number = 7 # A universally lucky number!
else:
    # Reduce the sum to a single digit or a small number for simplicity.
    # This is a common way to get a "destiny number" in numerology.
    # Keep summing digits until it's a single digit, or less than 100 for variety.
    while lucky_number_sum > 99: # Keep it interesting, not just single digit
        lucky_number_sum = sum(int(digit) for digit in str(lucky_number_sum))
    lucky_number = lucky_number_sum

# Display the personalized lucky number.
print(f"\nHello, {name}!")
print(f"Based on the magic of your name, your lucky number is: {lucky_number}!")
print("May it bring you good fortune today!")

# End of script.
```
