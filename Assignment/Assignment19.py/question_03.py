str1 = input("Enter the string: ")
count = sum([1 for ch in str1 if ch == " "])
print(count)