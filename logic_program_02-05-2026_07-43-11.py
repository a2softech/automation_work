```python
# This script tells you a fun fact about the number of vowels in a word you provide!

# Ask the user to enter a word
user_word = input("Enter a word: ")

# Convert the word to lowercase to easily count vowels (case-insensitive)
word_lower = user_word.lower()

# Define the vowels
vowels = "aeiou"

# Initialize a counter for vowels
vowel_count = 0

# Loop through each letter in the word
for letter in word_lower:
    # Check if the letter is one of the defined vowels
    if letter in vowels:
        vowel_count += 1 # Increment the counter if it's a vowel

# Print the original word and the count of vowels found
print(f"Your word '{user_word}' has {vowel_count} vowels.")

# Provide a simple "fun fact" based on the vowel count
if vowel_count == 0:
    print("Wow, no vowels at all! That's quite unique for a word!")
elif vowel_count == 1:
    print("Just one vowel! Simple and direct!")
elif vowel_count <= 3:
    print("A good number of vowels for balance!")
else:
    print("Many vowels! Your word sounds quite melodic!")
```
