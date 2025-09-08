emp = {
    'Name':'Rutika Patil',
    'Id':'@1812',
    'Dep':'SQL',
    'Address':'CSN',
    'Gender':'Female',
    'Salary':55000
}

key = input("Enter the which key-value is want: ")

if(key in emp):
    print(f"Key '{key}' is exists in dictionary.")
else:
    print(f"key '{key}' is not exist in dictionary.")

