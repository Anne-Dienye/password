import re

def password_checker(password):
    # Check length
    if not (8 <= len(password) <= 12):
        return "Invalid: Password must be between 8 and 12 characters long."
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Invalid: Password must contain at least one uppercase letter."
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Invalid: Password must contain at least one lowercase letter."
    
    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        return "Invalid: Password must contain at least one digit."
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Invalid: Password must contain at least one special character."
    
    # If all checks pass
    return "Valid: Password meets all requirements."

# Input from the user
password = input("Enter a password: ")

# Check the password
result = password_checker(password)
print(result)