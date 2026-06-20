```python
# Import the 'random' module to pick a random item from a list
import random

# A list of simple, encouraging words or phrases
encouraging_words = [
    "You got this!",
    "Keep learning!",
    "Great job!",
    "Stay curious!",
    "Fantastic!",
    "Almost there!",
    "Well done!",
    "You're a star!",
    "Keep coding!",
    "Awesome work!"
]

# Greet the user and explain the script's purpose
print("Welcome to your daily 'Python Encourager'!")
print("Let's get a random burst of positivity for your coding journey.")

# Wait for the user to press Enter, making it interactive
input("Press Enter to receive your encouragement...")

# Randomly select one encouraging word/phrase from our list
chosen_message = random.choice(encouraging_words)

# Print the chosen message to the user
print("\n--- Your Daily Boost ---")
print(chosen_message)
print("------------------------")
print("\nNow go build something amazing!")
```
