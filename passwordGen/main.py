import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type should be selected.")
        return

    if length < 1:
        print("Error: Password length should be at least 1.")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    return password

# Get user inputs
length = int(input("How long should the password be? "))
include_uppercase = input("Should it include uppercase letters? (y/n) ").lower() == "y"
include_lowercase = input("Should it include lowercase letters? (y/n) ").lower() == "y"
include_numbers = input("Should it include numbers? (y/n) ").lower() == "y"
include_symbols = input("Should it include symbols? (y/n) ").lower() == "y"

# Generate password
password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)
print("Generated Password:", password)
