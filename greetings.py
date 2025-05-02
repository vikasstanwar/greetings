from datetime import datetime

def greet_user():
    # Get the user's name
    name = input("Please enter your name: ")

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
    greet_user()
