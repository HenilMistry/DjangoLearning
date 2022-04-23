import string


def validateLower(password):
    valid = False
    for character in password:
        if character.islower():
            valid = True
            break
    return valid

def validateUpper(password):
    valid = False
    for character in password:
        if character.isupper():
            valid = True
            break
    return valid

def validateNumber(password):
    valid = False
    for character in password:
        if character.isdecimal():
            valid = True
            break
    return valid

def validateSpecial(password):
    specials = string.punctuation
    valid = False
    for character in password:
        if character in specials:
            valid = True
            break
    return valid

def validateLength(password):
    if len(password) < 6 or len(password) > 12:
        return False
    else:
        return True

def validatePassword(password):
    if not validateLower(password):
        print("At least one lower case letter must be present")
    elif not validateUpper(password):
        print("At least one upper case letter must be included")
    elif not validateNumber(password):
        print("At least one numeric letter must be included")
    elif not validateSpecial(password):
        print("At least one special letter must be included")
    elif not validateLength(password):
        print("Minimum length is 6 and maximum length is 12. Must follow this!")
    else:
        return True


listPassword = input("Enter testcases : ")
actual_list = listPassword.split(",")

valid_list = []
for password in actual_list:
    if validatePassword(password):
        valid_list.append(password)

for i in valid_list:
    print(i, end=", ")
