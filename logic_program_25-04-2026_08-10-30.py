```python
import random # Import the 'random' module to pick a random item later

# Ask the user for their name and store it in a variable called 'user_name'
user_name = input("Hey there! What's your name? ")

# Create a list (an ordered collection) of positive 'daily affirmations'
affirmations = [
    "You are capable of amazing things!",
    "Today is a new opportunity to shine.",
    "Your unique perspective is a valuable gift.",
    "Believe in yourself and all that you are.",
    "Small steps lead to great achievements.",
    "You have the power to create your own happiness.",
    "Embrace the journey, not just the destination.",
    "Your efforts are always worth it.",
]

# Randomly select one affirmation from the 'affirmations' list
chosen_affirmation = random.choice(affirmations)

# Print a personalized message using an f-string (formatted string literal)
# The f before the string allows you to embed variables directly using curly braces {}
print(f"\nHello, {user_name}! Here's a thought for you:")
print(f"✨ {chosen_affirmation} ✨")
print("\nRemember to have a fantastic day!")
```
