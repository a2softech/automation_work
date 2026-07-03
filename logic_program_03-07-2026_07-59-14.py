```python
# This script creates a simple, expanding and shrinking text art pattern.

# Ask the user for a single character or a short word to use in the pattern.
# The 'input()' function gets text from the user.
pattern_char = input("Enter a character or short word for your pattern: ")

# Ask the user for the maximum width of the pattern.
# 'int()' converts the user's text input into a whole number.
max_width = int(input("Enter the maximum width for the pattern (e.g., 7): "))

print("\n--- Expanding Pattern ---")
# This loop creates the expanding part of the pattern.
# 'range(1, max_width + 1)' generates numbers from 1 up to 'max_width'.
for i in range(1, max_width + 1):
    # 'pattern_char * i' repeats the character 'i' times.
    # 'print()' displays the result on a new line.
    print(pattern_char * i)

print("\n--- Shrinking Pattern ---")
# This loop creates the shrinking part of the pattern.
# 'range(max_width - 1, 0, -1)' counts down from 'max_width - 1' to 1.
# The last '-1' means step backwards.
for i in range(max_width - 1, 0, -1):
    # Again, repeat the character 'i' times.
    print(pattern_char * i)

# A final message to indicate the script has finished.
print("\nPattern complete!")
```
