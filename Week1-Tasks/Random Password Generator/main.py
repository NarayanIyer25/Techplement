import random
print("Random Password Generator")
Capital_Letters = ['A','B','C','D','E','F','G','H','I','J',
                   'K','L','M','N','O','P','Q','R','S','T',
                   'U','V','W','X','Y','Z']
Small_Letters = ['a','b','c','d','e','f','g','h','i','j',
                   'k','l','m','n','o','p','q','r','s','t',
                   'u','v','w','x','y','z']
digits = ['0','1','2','3','4','5','6','7','8','9']
Special_Characters = ['!','@','#','$','^','&','*','(',')']
user_upper_case = int(input("Enter the number of Uppercase Letters: "))
user_lower_case = int(input("Enter the number of Lowercase Letters: "))
user_digits = int(input("Enter the number of Digits: "))
user_special_character = int(input("Enter the number of Special Characters: "))
def RandomPasswordGenerator(user_upper_case,user_lower_case,user_digits,user_special_character):
    password = ''
    password_upper_case = ''
    password_lower_case = ''
    password_digits = ''
    password_special_characters = ''
    for i in range(user_upper_case):
        password_upper_case += random.choice(Capital_Letters)

    for i in range(user_lower_case):
        password_lower_case += random.choice(Small_Letters)

    for i in range(user_digits):
        password_digits += random.choice(digits)

    for i in range(user_special_character):
        password_special_characters += random.choice(Special_Characters)

    final_password = password_lower_case+password_special_characters+password_upper_case+password_digits
    for i in range(len(final_password)):
        password += random.choice(final_password)
    return password

final_password = RandomPasswordGenerator(user_upper_case,user_lower_case,user_digits,user_special_character)
print(f'Your Final Password is {final_password}')