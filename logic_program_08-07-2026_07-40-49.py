```python
# Import the 'random' module to pick a random item from a list later.
import random

# A list of short, positive affirmations or 'fortune cookie' style messages.
# Each item in the list is a string (text).
messages = [
    "Today is your day to shine!",
    "Believe in yourself and all that you are.",
    "Embrace new challenges with an open mind.",
    "Small steps lead to great journeys.",
    "Your unique perspective is a gift.",
    "Spread kindness wherever you go.",
    "Find joy in the simple moments.",
    "You are capable of amazing things.",
    "Growth often comes from unexpected places.",
    "Listen to your intuition today."
]

# Print a welcoming message to the user.
print("--- Daily Thought Generator ---")
print("Press Enter to receive your positive thought for the day.")

# Use the input() function to pause the script until the user presses Enter.
# The actual input isn't used, just the action of pressing the key.
input() 

# Use random.choice() to select one random message from the 'messages' list.
chosen_message = random.choice(messages)

# Print the selected message to the console.
print("\n--- Your Thought ---")
print(chosen_message)
print("--------------------")

# A final encouraging message.
print("\nHave a wonderful day!")
```
