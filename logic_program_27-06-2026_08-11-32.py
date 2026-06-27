```python
# This script generates a random compliment just for you!

import random # We need this to pick random items from lists.

# Create a list of different ways a compliment can start.
compliment_starts = [
    "You're an amazing",
    "Your presence makes everyone",
    "I bet your smile could brighten",
    "You have a truly wonderful",
    "It's impressive how you always manage to be such a",
    "Anyone would be lucky to have a friend as",
    "Your unique perspective is a",
]

# Create a list of different ways a compliment can end or describe someone.
compliment_ends = [
    "person!",
    "feel better!",
    "the darkest room!",
    "sense of humor!",
    "thoughtful individual!",
    "supportive person as you!",
    "gift!",
    "shining star!",
    "problem-solver!",
]

# Choose one random start phrase from our list.
selected_start = random.choice(compliment_starts)

# Choose one random end phrase from our list.
selected_end = random.choice(compliment_ends)

# Combine the chosen start and end to form a complete compliment.
# An f-string (formatted string literal) is used here to easily embed variables.
full_compliment = f"{selected_start} {selected_end}"

# Print a friendly message and then your unique compliment!
print("\nHere's a little something positive for your day:")
print("✨", full_compliment, "✨") # We add some sparkles for extra cheer!
print("\nHave a fantastic day!")
```
