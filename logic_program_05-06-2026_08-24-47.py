```python
import random

# This script generates a random fun fact or a kind compliment!

# A list of interesting facts
fun_facts = [
    "A group of owls is called a parliament.",
    "Honey never spoils.",
    "It is impossible for most people to lick their own elbow.",
    "Sharks have been around longer than trees.",
    "The shortest war in history lasted 38 to 45 minutes."
]

# A list of encouraging compliments
compliments = [
    "You're doing great!",
    "Your smile is contagious!",
    "You have excellent taste.",
    "You light up the room!",
    "You're incredibly kind."
]

print("Welcome! Let's get a random message for you.")

# Randomly choose between showing a fact (True) or a compliment (False)
# random.choice picks one item from a given list
if random.choice([True, False]):
    # If True, pick a random fact from our fun_facts list
    selected_message = random.choice(fun_facts)
    print(f"\nHere's a fun fact: {selected_message}")
else:
    # If False, pick a random compliment from our compliments list
    selected_message = random.choice(compliments)
    print(f"\nHere's a compliment for you: {selected_message}")

print("\nHave a wonderful day!")
```
