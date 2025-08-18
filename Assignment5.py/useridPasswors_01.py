CORRECT_USERID = "komal"
CORRECT_PASSWORD = "992270"

for attempt in range(1, 3):
    userid = input("Enter the userid: ")
    password = input("Enter the password: ")

    if(userid == CORRECT_USERID and password == CORRECT_PASSWORD):
        print("Login Successful!")
        break
    else:
        print(f'Invalid credential!. Attempt left{2 - attempt}')
else:
    print(f'Too many failed attempts. Program terminated.')