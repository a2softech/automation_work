```python
# This script creates a tiny, personalized, and randomized story!

import random # We use the 'random' module to pick things randomly later.

print("Welcome to the Tiny Tale Creator!")
print("Let's make a silly story together.")

# Ask the user for two words to make the story unique.
user_adjective = input("Give me an adjective (e.g., 'sparkling', 'sleepy'): ")
user_noun = input("Now, how about a noun (e.g., 'dragon', 'teacup'): ")

# Define lists of possible actions and outcomes for our story character.
possible_actions = [
    "discovered a hidden path",
    "sang a silly song",
    "chased a butterfly",
    "built a tiny castle",
    "solved a tricky puzzle"
]

possible_outcomes = [
    "and found a treasure!",
    "but then tripped over a banana peel.",
    "leading to a grand adventure!",
    "and was very proud of their work.",
    "which made everyone cheer loudly!"
]

# Randomly pick one action and one outcome from our lists.
chosen_action = random.choice(possible_actions)
chosen_outcome = random.choice(possible_outcomes)

# Print the complete story using the user's words and our random choices.
# We use an f-string (formatted string literal) for easy text combining.
print("\n--- Your Tiny Tale ---")
print(f"Once upon a time, a {user_adjective} {user_noun} {chosen_action} {chosen_outcome}")
print("The end.")
print("--------------------")
```
