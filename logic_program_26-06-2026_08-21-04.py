```python
# This script asks for your name and then greets you.
# It also calculates the length of your name.

# Get the user's name as input.
# The input() function waits for the user to type something and press Enter.
user_name = input("What's your name? ")

# Print a personalized greeting using the name provided.
# f-strings (formatted string literals) are a modern way to embed variables in strings.
print(f"Hello, {user_name}! It's great to meet you.")

# Calculate the number of characters in the name.
# The len() function returns the length of a string.
name_length = len(user_name)

# Display how many letters are in their name.
print(f"Did you know your name has {name_length} letters?")

# A small farewell message.
print("Have a fantastic day!")
```
