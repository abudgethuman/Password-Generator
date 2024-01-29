import random
from colorama import Fore, Style, init

init(autoreset=True)

CHARACTER_SETS = {
    '1': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    '2': "abcdefghijklmnopqrstuvwxyz",
    '3': "1234567890",
    '4': "!@#$%^&*",
}
DEFAULT_LENGTH = 8

def pass_gen(length, char_types):
    selected_chars = ''.join(CHARACTER_SETS[char_type] for char_type in char_types)
    result = ''.join(random.choice(selected_chars) for _ in range(length))

    print(f"\nYour password is: {Fore.GREEN}{result}")

def get_valid_length():
    while True:
        length_str = input(f"{Fore.CYAN}Enter password length (press Enter for default length): ")
        if not length_str:
            return DEFAULT_LENGTH
        try:
            length = int(length_str)
            if length > 0:
                return length
            else:
                print(f"{Fore.RED}Please enter a positive integer for the password length.")
        except ValueError:
            print(f"{Fore.RED}Invalid input. Please enter a valid number for the password length.")

def get_valid_char_types():
    allowed_char_types = set("1234")
    while True:
        chars_to_include = input(f"""{Fore.CYAN}\n
Characters to include in your password:
=======================================
[1] Uppercase  [3] Numbers
[2] Lowercase  [4] Symbols

Enter the numbers of the types you want (e.g., "1234"): """)
        
        if all(char_type in allowed_char_types for char_type in chars_to_include):
            return chars_to_include
        else:
            print(f"{Fore.RED}Invalid input. Please enter valid types.")

length = get_valid_length()
chars_to_include = get_valid_char_types()

pass_gen(length, chars_to_include)
