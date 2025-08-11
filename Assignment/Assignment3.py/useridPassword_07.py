userid = input("Enter the username: ")
password = int(input("Enter the password: "))

login_userid = "Komal_Patil"
login_password = 99181225

if((login_userid == userid) and (login_password == password)):
# if(("Komal Patil" == userid) and (99181225 == password)):
    print(f'{userid} and {password} is entered correct userid and  password')

else:
    print(f'{userid} and {password} is not correct')

