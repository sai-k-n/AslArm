import re
from gesture import *

# Get input
while True:
    # Get input from user and convert to uppercase
    inputString = input("Enter a string: ").upper()

    # Check if input string matches regex (ABC and spaces)
    if re.fullmatch(r"[A-Z ]+", inputString):
        # Loop through all letters
        for letter in list(inputString):
            try:
                # Get gesture with string
                globals()[f"gesture{letter}"]()
            except:
                # On the event that the associated gesture is not found, throw an error instead of crashing app
                print("*space*")
    else:
        # If the string contains anything other than ABC and spaces throw error
        print("String includes charcters the are not allowed!")