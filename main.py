def check_password_len(password):
    if len(password) < 8:
        return False
    else: return True
    
def check_character_types(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
    
    return {
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_number": has_number,
        "has_special": has_special
    }

def list_common_passwords():
    try:
        with open("10k-most-common.txt", "r") as file:
            return [line.strip().lower() for line in file]
    except FileNotFoundError:
        print("Warning: Common passwords file not found. Skipping common password check.")
        return []
    

def check_common(password, list):
    return password.lower() in list


def main():
    common_list = list_common_passwords()
    max_score = 5
    password = input("Enter password: ")
    if not check_common(password, common_list):
        if not check_password_len(password):
            print("Password is too short! It must be at least 8 characters!")
        else:
            print("Password length is valid.")
            strengthScore = 1

            character_checks = check_character_types(password)
            strengthScore += sum(character_checks.values())
            if all(character_checks.values()):
                print("Password is strong!")
            else:
                print("Password is weak! Missing the following:")
                if not character_checks["has_upper"]:
                    print("- Uppercase letter")
                if not character_checks["has_lower"]:
                    print("- Lowercase letter")
                if not character_checks["has_number"]:
                    print("- Number")
                if not character_checks["has_special"]:
                    print("- Special character")
            print(f"Strength score of password: {strengthScore}/{max_score}")
    else:
        print("Your password is too common! Please choose a more unique password!")   
        print("Strength score of password: 0/5") 

main()