```python
# This script creates a simple "emoji weather reporter"!

import random

# Ask the user for today's temperature
temperature_str = input("What's the temperature outside (in Celsius)? ")

# Convert the temperature input from string to an integer number
# This might cause an error if the user doesn't enter a valid number,
# but for a beginner script, we'll assume valid input.
temperature = int(temperature_str)

# Define a list of possible weather emojis
sun_emojis = ["☀️", "🌤️", "😎"]
cloud_emojis = ["☁️", "🌫️", "🌬️"]
rain_emojis = ["🌧️", "💧", "☔"]
snow_emojis = ["❄️", "🌨️", "☃️"]

# Decide the weather emoji based on the temperature
if temperature >= 25:
    # If it's warm, pick a sunny emoji
    weather_emoji = random.choice(sun_emojis)
    feeling_text = "It's a warm one!"
elif temperature >= 15:
    # If it's mild, pick a cloudy emoji
    weather_emoji = random.choice(cloud_emojis)
    feeling_text = "Quite mild today."
elif temperature >= 5:
    # If it's cool, pick a rainy emoji (could be anything really, just an example)
    weather_emoji = random.choice(rain_emojis)
    feeling_text = "A bit chilly, might need a jacket."
else:
    # If it's cold, pick a snowy emoji
    weather_emoji = random.choice(snow_emojis)
    feeling_text = "Brrr! It's cold out there."

# Print the weather report using an f-string
print(f"Today's weather report: {weather_emoji} {feeling_text}")
print("Stay safe and enjoy your day!")
```
