emp = {
    'Name':'Komal Patil',
    'Id':'ql2025',
    'Dep':'Python',
    'Salary':70000,
    'Address':'Pune',
    'Gender':'Female'
}

key = input("Enter the key: ")

if(key in emp):
    del_data= emp.pop(key)
    print(f"key '{key}' is remove value is '{del_data}'.")
else:
    print(f"key '{key}' is not present in dictionary.")

print("Updated dictinaty: ",emp)