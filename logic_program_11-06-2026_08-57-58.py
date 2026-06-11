```python
import random # Import the 'random' module to generate random numbers and choices.
import time   # Import the 'time' module to pause the script.

# --- "Mystic Orb" Fortune Teller ---
# This script simulates a simple fortune-telling orb.

print("Welcome, Seeker! I am the Mystic Orb of Python.")
time.sleep(1) # Pause for 1 second to make the interaction feel more natural.
print("Ask me a yes/no question, and I shall reveal your fate...")
time.sleep(1.5)

# Get the user's question. We don't actually process the question,
# but it makes the interaction feel more personal.
user_question = input("\nYour question for the Orb: ")

print("\nConsulting the cosmic energies...")
time.sleep(2) # A longer pause for dramatic effect.

# Define a list of possible answers.
# Lists are ordered collections of items.
fortunes = [
    "It is certain.",
    "Without a doubt.",
    "You may rely on it.",
    "Yes, definitely.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

# Use random.choice() to select one random fortune from the 'fortunes' list.
# This demonstrates how to pick a random item from a collection.
chosen_fortune = random.choice(fortunes)

# Print the chosen fortune to the user.
print(f"The Mystic Orb reveals: {chosen_fortune}") # f-strings are a neat way to embed variables in strings.

time.sleep(1)
print("\nMay your path be clear, Seeker!")
```
