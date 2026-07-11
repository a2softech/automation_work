```python
import time # We need the 'time' module to make the script pause for a short duration.

# This line asks the user for some text and stores it in a variable called 'user_message'.
user_message = input("Type a short message to see it wave: ")

# This variable sets the total width of the 'screen' where our text will move.
# Think of it as the maximum number of spaces available for the wave.
wave_width = 50

# This print statement adds an empty line for better spacing and tells the user what's happening.
print("\nStarting the text wave...\n")

# We'll make the wave animation loop a few times so you can see it clearly.
# 'range(3)' means the loop will run 3 times (for cycle = 0, 1, 2).
for cycle in range(3):
    # --- Part 1: Make the text wave from left to right ---
    # We loop from 0 up to (wave_width - length of user_message - 1).
    # This ensures the text stops before going off the right edge.
    for i in range(wave_width - len(user_message)):
        # We print 'i' number of spaces, followed by our user's message.
        # 'end="\r"' is a special trick! It tells Python to move the cursor
        # back to the beginning of the current line instead of starting a new line.
        # This makes the new print overwrite the old one, creating the animation effect.
        print(" " * i + user_message, end="\r")
        
        # We pause for a very short time (0.07 seconds) so you can see the movement.
        time.sleep(0.07)

    # --- Part 2: Make the text wave from right to left ---
    # Now we loop backwards, from (wave_width - length of user_message - 1) down to 0.
    # The '-1' as the third argument in range means we count down one step at a time.
    for i in range(wave_width - len(user_message) - 1, -1, -1):
        # Again, we print spaces followed by the text, overwriting the previous line.
        print(" " * i + user_message, end="\r")
        time.sleep(0.07) # Another short pause.

# After all cycles are done, print a final message and ensure it's on a new line.
print("\n\nText wave complete! Hope you enjoyed the show.")
```
