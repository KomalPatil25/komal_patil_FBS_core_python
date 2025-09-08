# dict ={}

# dict.update({'Name':'Komal', 'age':18, 'address':'pune', 'degree':'BCA'})
# print(dict)

dict ={}
num = int(input("Enter the number to how may key=value pairs want to add in dictionary: "))
for i in range(num):
    key = input("Enter the key: ")
    value = input("Enter the value: ")

    dict[key] = value

print("Updated dictionary: ",dict)
