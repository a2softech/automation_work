```python
# This script takes text from you and puts it in a fun ASCII art box!

# Get input from the user. The text they type will be stored in the 'user_text' variable.
user_text = input("Enter some text to put in an ASCII box: ")

# Calculate the length of the text. This helps us make the box fit perfectly.
text_length = len(user_text)

# Determine the total width of the box.
# We add 4: 1 for the left border '*', 1 for the left space, 1 for the right space, 1 for the right border '*'.
# Example: "hello" (5 chars) needs 5+4=9 width: "**** hello ****"
box_width = text_length + 4

# Create the top and bottom border line.
# It's a string of '*' characters repeated 'box_width' times.
border_line = "*" * box_width

# Print the top border line.
print(border_line)

# Print the line with the user's text inside.
# It starts with '*', then a space, then the user's text, then another space, and finally '*'.
# We use an f-string (formatted string literal) for easy and readable text embedding.
print(f"* {user_text} *")

# Print the bottom border line, which is the same as the top.
print(border_line)

# End of script!
```
