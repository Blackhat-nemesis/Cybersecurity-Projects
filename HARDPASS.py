import re
import random
from termcolor import colored

def generate_logo():
    logo = """
    
██╗░░██╗░█████╗░██████╗░██████╗░██████╗░░█████╗░░██████╗░██████╗
██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
███████║███████║██████╔╝██║░░██║██████╔╝███████║╚█████╗░╚█████╗░
██╔══██║██╔══██║██╔══██╗██║░░██║██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗
██║░░██║██║░░██║██║░░██║██████╔╝██║░░░░░██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░ 
    """
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    for line in logo.split("\n"):
        print(colored(line, random.choice(colors)))

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    number_criteria = bool(re.search(r"\d", password))
    special_char_criteria = bool(re.search(r"[@$!%*?&]", password))
    
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    if score <= 2:
        return colored("Weak", "red")
    elif score == 3 or score == 4:
        return colored("Moderate", "yellow")
    else:
        return colored("Strong", "green")

def main():
    generate_logo()
    print(colored("Welcome to HARDPASS - The Ultimate Password Strength Checker!", "cyan"))
    
    while True:
        password = input("\nEnter your password (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print(colored("Goodbye! Stay safe online!", "magenta"))
            break
        
        strength = check_password_strength(password)
        print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
