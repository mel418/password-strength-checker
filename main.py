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
    file = open("10k-most-common.txt", "r")
    common_passwords = []
    for line in file:
        common_passwords.append(line.strip())
    file.close()
    return common_passwords

def main():
    max_score = 5
    password = input("Enter password: ")
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
        print(list_common_passwords())

main()