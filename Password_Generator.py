import re
import secrets
import string

length1 = int(input('How many characters should your password be? '))

nums1 = int(input('How many numbers should your password have? '))
if nums1 > length1:
  print('You entered more characters than the length of the password, exiting program')
  exit()

special_chars1 = int(input('How many special characters should your password have? '))
if nums1 + special_chars1 > length1:
  print('You entered more characters than the length of the password, exiting program')
  exit()

uppercase1 = int(input('How many capitalized characters should your password have? '))
if nums1 + special_chars1 + uppercase1 > length1:
  print('You entered more characters than the length of the password, exiting program')
  exit()

lowercase1 = int(input('How many lowercase characters should your password have? '))
if nums1 + special_chars1 + uppercase1 + lowercase1 > length1:
  print('You entered more characters than the length of the password, exiting program')
  exit()

def generate_password(length, nums, special_chars, uppercase, lowercase):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password

if __name__ == '__main__':
    new_password = generate_password(length1, nums1, special_chars1, uppercase1, lowercase1)
    print('Generated password:', new_password)