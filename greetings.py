#!/usr/bin/env python3
import sys
from datetime import datetime

def greet_user(name):
    # Get the current hour
    current_hour = datetime.now().hour

    # Determine the appropriate greeting
    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    # Print the greeting
    print(f"{greeting}, {name}!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python greetings.py <name>")
        sys.exit(1)
    name = sys.argv[1]
    greet_user(name)
