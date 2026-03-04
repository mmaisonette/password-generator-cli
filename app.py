"""
Password Generator Module

A command-line utility for generating secure random passwords with customizable
length and character set options.

This module provides functionality to:
- Generate random passwords of specified length (20-40 characters)
- Optionally exclude ambiguous characters (O/0, l/1, etc.)
- Copy generated passwords to the system clipboard

Functions:
    build_alphabet: Constructs the character set for password generation
    password_generator: Main function that handles user input and password generation

Dependencies:
    - string: For character set definitions
    - secrets: For cryptographically secure random selection
    - pyperclip: For clipboard operations

Usage:
    Run the module directly to start the interactive password generator:
    $ python app.py
"""

import string
import secrets
import pyperclip


def build_alphabet(avoid_ambiguous=False):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    if avoid_ambiguous:
        ambiguous = set("O0oIl1|")
        alphabet = "".join(ch for ch in alphabet if ch not in ambiguous)
    return alphabet


def password_generator():
    try:
        length = int(
            input("\nHow many characteres do you want in your new password? ").strip()
        )
    except ValueError:
        return "\nYou must submit the number of characters you want using numbers!"

    if not 20 <= length <= 40:
        print("\nLength must be between 20 and 40!")
        return None

    try:
        avoid_ambiguous = (
            input("\nAvoid ambiguous characters (O/0, l/1)? [y/N]: ").strip().lower()
            == "y"
        )
    except ValueError:
        return "\nYou must submit y(yes) or N(no)!"

    alphabet = build_alphabet(avoid_ambiguous)
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    return password


if __name__ == "__main__":
    password_generated = password_generator()

    if password_generated is not None:
        print(password_generated)

        copy_choice = input("\nCopy password to clipboard? [y/N]: ").strip().lower()
        if copy_choice == "y":
            try:
                pyperclip.copy(password_generated)
                print("\nPassword copied to clipboard!")
            except pyperclip.PyperclipException:
                print("Could not access clipboard on this system.")
