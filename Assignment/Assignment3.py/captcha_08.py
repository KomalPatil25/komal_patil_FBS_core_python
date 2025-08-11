import random

userid = input("Enter the username: ")
password = int(input("Enter the password: "))

captcha = random.randint(1111, 9999)
print(f'Captcha: {captcha}')

user_captcha = int(input("Enter the captcha again: "))
# login_userid = "Komal_Patil"
# login_password = 99181225

# if((login_userid == userid) and (login_password == password)):
if(("Komal Patil" == userid) and (99181225 == password)):
    if(user_captcha == captcha):
        print(f'success! Access granted')
    else:
        print(f'captcha is wrong')
#     print(f'{userid} and {password} is entered correct userid and  password')

# else:
#     print(f'{userid} and {password} is not correct')
