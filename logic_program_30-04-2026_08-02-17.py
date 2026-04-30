```python
import time
import random

# This script creates a simple, unique "mood ring" using text.
# It changes the "color" (character) and "intensity" (number of characters)
# based on a simulated mood.

print("Welcome to your digital mood ring!")
print("Press Ctrl+C to stop at any time.")

# Define possible "mood colors" (characters) and their associated "moods"
MOOD_COLORS = {
    "happy": "✨",
    "calm": "💧",
    "energetic": "🔥",
    "pensive": "💭",
    "mysterious": "🔮",
    "sleepy": "💤",
    "neutral": "⚪"
}

# Define the range for "intensity" (how many characters are displayed)
MIN_INTENSITY = 3
MAX_INTENSITY = 15

# Simulate a continuously changing mood
while True:
    # Pick a random mood from our defined list
    current_mood_name = random.choice(list(MOOD_COLORS.keys()))
    current_mood_char = MOOD_COLORS[current_mood_name]

    # Pick a random intensity for the current mood
    current_intensity = random.randint(MIN_INTENSITY, MAX_INTENSITY)

    # Create the mood ring display string
    # String multiplication makes it easy to repeat characters
    mood_display = current_mood_char * current_intensity

    # Print the current mood and its display
    # The `f-string` (formatted string literal) is a modern way to embed variables
    print(f"[{current_mood_name.upper():<10}] {mood_display}")

    # Pause for a short time before changing mood again
    # This makes the changes visible and not too fast
    time.sleep(1.5) # Wait 1.5 seconds
```
