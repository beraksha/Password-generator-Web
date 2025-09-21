import random
import string

def generate_password(length=12, include_uppercase=True, include_digits=True, include_symbols=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected."

    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    desired_length = int(input("Enter desired password length: "))
    password = generate_password(length=desired_length)
    print(f"Generated password: {password}")