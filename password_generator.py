import random
import string

def generate_password(length=12):
    # Characters to use: uppercase, lowercase, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("=== SIMPLE PASSWORD GENERATOR ===")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
    except ValueError:
        print("Invalid input, using default length 12.")
        length = 12

    password = generate_password(length)
    print(f"\nYour generated password is: {password}")
