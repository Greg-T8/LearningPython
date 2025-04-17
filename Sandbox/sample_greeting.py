def greet_user():
    name = input("What's your name? ")
    print(f"Hello, {name}!")

def check_age():
    try:
        age = int(input("How old are you? "))
        if age < 18:
            print("You're a minor.")
        elif age < 65:
            print("You're an adult.")
        else:
            print("You're a senior citizen.")
    except ValueError:
        print("Please enter a valid number.")

# Main program
greet_user()
check_age()

print("Thank you for using the greeting program!")

