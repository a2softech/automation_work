```python
# This script creates a tiny, personalized story based on your inputs!

# First, we'll ask the user for a few words.
# The input() function prompts the user and captures their text.

# Get an adjective (describing word)
adjective = input("Enter an adjective (e.g., 'bright', 'sleepy'): ")

# Get a noun (person, place, thing, or idea)
noun = input("Enter a noun (e.g., 'river', 'dragon'): ")

# Get a verb (action word)
verb = input("Enter a verb (e.g., 'dances', 'whispers'): ")

# Get a sound
sound = input("Enter a sound (e.g., 'buzz', 'chirp'): ")

# Now, let's put all the words together into a fun, short story.
# We'll use f-strings, which are a simple way to embed variables directly into strings.
print("\n--- Your Tiny Tale ---")
print(f"In a world where the {adjective.lower()} {noun.lower()} always {verb.lower()},")
print(f"a strange little {sound.upper()} echoed through the air.")
print("Everyone stopped to listen.")
print("The End.")
print("--------------------")

# A final message for the user.
print("\nHope you enjoyed your custom story!")
```
