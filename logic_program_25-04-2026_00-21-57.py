```python
# This script creates a simple "Mad Libs" style story with user input.

# First, we'll ask the user for different types of words.
# The input() function gets text from the user.

# Ask for a noun (a person, place, or thing)
noun1 = input("Enter a noun (e.g., 'cat'): ")

# Ask for an adjective (a descriptive word)
adjective1 = input("Enter an adjective (e.g., 'sleepy'): ")

# Ask for a verb (an action word)
verb1 = input("Enter a verb (e.g., 'run'): ")

# Ask for another noun
noun2 = input("Enter another noun (e.g., 'mountain'): ")

# Now, we'll put all these words into a simple story.
# We use f-strings to easily insert our variables into the text.
print("\n--- Your Story ---") # The '\n' creates a new line for better readability.

story = f"The {adjective1} {noun1} decided to {verb1} all the way to the {noun2}."

# Print the complete story.
print(story)

print("--- End of Story ---")
```
