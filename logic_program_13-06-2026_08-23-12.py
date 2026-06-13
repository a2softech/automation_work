```python
# This script helps you choose a random snack from a small list!

import random # We need the 'random' module to pick something randomly.

# A list of snack ideas. You can change these to your favorites!
possible_snacks = [
    "Apple slices with peanut butter",
    "A handful of almonds",
    "Yogurt with berries",
    "Carrot sticks and hummus",
    "Rice cakes with avocado",
    "A banana",
    "Popcorn (air-popped)",
    "Hard-boiled egg",
]

# Print a friendly message to the user.
print("Feeling hungry? Let's pick a healthy snack for you!")
print("---")

# Use random.choice() to pick one item from our list.
chosen_snack = random.choice(possible_snacks)

# Display the chosen snack.
print(f"How about: {chosen_snack}!")

print("---")
print("Enjoy your snack!")
```
