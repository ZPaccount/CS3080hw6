"""
Homework 6-3
Name: Zachary Pace
Date: 3/30/2023
Description: hold multiple clipboards
"""
# Imports
import clipboard as c
import re

running = True
List = {}
while running:
    # Input command line
    command = input("Input Your Command:")
    # Save clipboard
    if re.match(r"python3 mcb.py save", command):
        command = command[20:]
        List[command] = c.paste()
    # List all Clipboards saved
    elif re.match(r"python3 mcb.py list", command):
        print(List)
    # copy predetermined Clipboard item
    elif re.match(r"python3 mcb.py", command):
        command = command[15:]
        c.copy(List[command])
    # Added for testing end command
    elif re.match(r"end", command):
        running = False
