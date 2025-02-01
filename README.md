# Password Strength Checker

## Overview
A Python-based **Password Strength Checker** with a Tkinter GUI. It evaluates passwords based on:
- **Length** (minimum 8 characters).
- **Character types** (uppercase, lowercase, numbers, special characters).
- **Common passwords** (checks against `10k-most-common.txt`).

Provides feedback and a strength score out of 5.

---

## Features
- **Password Strength Evaluation**: Checks length, character types, and common passwords.
- **GUI**: Built with Tkinter (input field, buttons, result display).
- **Common Password Check**: Compares against a list of 10,000 common passwords.

---

## How to Use
1. Run the script:
   ```bash
   python password_strength_checker.py

## What I Learned
- **Tkinter Basics**: Creating GUIs with labels, buttons, and input fields.

- **Password Logic**: Checking length, character types, and common passwords.

- **File Handling**: Reading from a text file for common passwords.

- **User Feedback**: Displaying results dynamically in the GUI.

I want to improve it with password entropy later on
(https://nordvpn.com/blog/what-is-password-entropy/#:~:text=Password%20entropy%20is%20the%20measure,that%20takes%20ages%20to%20crack.)
