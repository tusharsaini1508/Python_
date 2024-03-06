import re
def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_=+`~,<>.?/:;{}[\]|]).{8,32}$"
    return bool(re.match(pattern, password))
while True:
    password = input("Enter your password: ")
    if is_valid_password(password):
        print("Valid password")
    else:
        print("Invalid password")
