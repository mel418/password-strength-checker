import tkinter as tk

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


def password_strength():
    common_list = list_common_passwords()
    max_score = 5
    password = entry.get()

    if check_common(password, common_list):
        return "Your password is too common! Please choose a more unique password!\nStrength score of password: 0/5"
    else:
        if not check_password_len(password):
            return "Password is too short! It must be at least 8 characters!"
        else:
            strengthScore = 1
            character_checks = check_character_types(password)
            strengthScore += sum(character_checks.values())

            if all(character_checks.values()):
                return f"Password is strong!\nStrength score of password: {strengthScore}/{max_score}"
            else:
                feedback = "Password is weak! Missing the following:\n"
                if not character_checks["has_upper"]:
                    feedback += "- Uppercase letter\n"
                if not character_checks["has_lower"]:
                    feedback += "- Lowercase letter\n"
                if not character_checks["has_number"]:
                    feedback += "- Number\n"
                if not character_checks["has_special"]:
                    feedback += "- Special character\n"
                feedback += f"Strength score of password: {strengthScore}/{max_score}"
                return feedback


# create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# add a label
label = tk.Label(root, text="Enter your password: ")
label.pack()

# add an input field
entry = tk.Entry(root, show="*") # show '*' for password input
entry.pack()

def on_check():
    result = password_strength()
    result_label.config(text=result) # update the result label

# function to clear the input field
def on_clear():
    entry.delete(0, tk.END) # clear the input field
    result_label.config(text="") # clear the result label

# add a button
button = tk.Button(root, text="Check Strength", command=on_check)
button.pack()

clear_Button = tk.Button(root, text="Clear", command=on_clear)
clear_Button.pack()

# add a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# run the app
root.mainloop()





