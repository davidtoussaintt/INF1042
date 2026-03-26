
def is_valid_password(password):
    has_digit = False
    has_letter = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isalpha():
            has_letter = True

    if len(password) >= 8 and has_digit and has_letter:
        return True
    else:
        return False
    
password = input("Enter a password: ")


if is_valid_password(password):
    print("Valid")
else:
    print("Invalid")