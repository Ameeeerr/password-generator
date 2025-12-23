import random

# Pool of characters
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

play_again = "yes"

while play_again in ("yes", "y"):
    password = ""
    pool = letters

    length = int(input("How long would you like the password? "))
    nums = input("Include numbers? (y/n): ").lower()
    symbols2 = input("Include symbols? (y/n): ").lower()

    if nums == "y":
        pool += numbers
    if symbols2 == "y":
        pool += symbols

    for _ in range(length):
        password += random.choice(pool)

    print("Generated password:", password)

    play_again = input("Generate another password? (yes/no): ").lower()
