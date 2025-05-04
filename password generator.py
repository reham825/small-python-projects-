#ask the user about the password length
#ask the user if the password include uppercase letters
#ask the user if the password include numbers
#ask the user if the password include special characters
import string
import random
def generate_password(length_of_password, include_uppercase, include_numbers, include_specialcharacters):
    if length_of_password < len(include_uppercase+include_numbers+include_specialcharacters):
        raise ValueError("password length is too short to the specified criteria.")
    password = []
    if include_uppercase == 'y':
        password.append(random.choice(string.ascii_uppercase))
    if include_numbers == 'y':
        password.append(random.choice(string.digits))
    if include_specialcharacters == 'y':
        password.append(random.choice(string.punctuation))
    if len(password) < length_of_password:
        characters = ""
        characters += string.ascii_lowercase
        if include_uppercase == 'y':
            characters += string.ascii_uppercase
        if include_numbers == 'y':
            characters += string.digits
        if include_specialcharacters == 'y':
            characters += string.punctuation
        for i in range(length_of_password-len(password)):
            password.append(random.choice(characters))
        password = ''.join(password)


    return password

length_of_password = int(input("Enter the length of the password: \n"))
include_uppercase = input("do you like to include uppercase letters? (y/n) \n").lower()
include_numbers = input("do you like to include numbers? (y/n) \n").lower()
include_specialcharacters = input("do you like to include special characters? (y/n) \n").lower()


password = generate_password(length_of_password,
                             include_uppercase,
                             include_numbers,
                             include_specialcharacters)
print(f'password is "{password}"')