```python
# This script creates a unique little message based on your imagination!

# We'll ask you for a few words to make it personal.
# Each word you type will be stored in a 'variable'.
# 'input()' lets you type something, and 'print()' shows text on the screen.

animal = input("Think of an animal (e.g., 'squirrel'): ")
adjective = input("Now, an adjective (e.g., 'sparkling'): ")
action = input("Finally, a verb describing an action (e.g., 'dances'): ")

# Now, let's put your words together into a special message!
# We use 'f-strings' (the 'f' before the quotes) to easily insert your variables.
print("\n--- Your Magical Message ---")
print(f"A {adjective} {animal} just appeared!")
print(f"It happily {action} under the moonlit sky.")
print("What a wonderful and unexpected sight!")
print("--- End of Message ---")

# Try running the script again with different words to see a new message!
```
