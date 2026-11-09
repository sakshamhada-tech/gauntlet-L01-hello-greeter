from datetime import date

def ask_name():
    while True:
        first_name = input("\nWhat is your first name? ").strip().title()

        if first_name.isalpha():
            break

    while True:
        last_name = input("\nWhat is your last name? ").strip().title()

        if last_name.isalpha():
            break

    name = first_name + " " + last_name

    return name

def ask_age():
    current_year = date.today().year
    while True:
        try:
            birth_year = int(input("\nWhat is your birth year? "))
        except ValueError:
            print("\nPlease enter your birth year in integer.")
            continue
        if current_year - birth_year >= 0 and current_year - birth_year <= 120:
            break
        else:
            print("\nPlease enter your correct birth year!")

    return current_year - birth_year


name = ask_name()
age = ask_age()

print(f"\nHello there, {name}! You are about {age} years old.")

