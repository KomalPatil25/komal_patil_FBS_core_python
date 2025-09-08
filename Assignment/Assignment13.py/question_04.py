dict = {}

n = int(input("Enter the number: "))
for i in range(1, n + 1):
    result = i * i
    dict.update({i : result})

print(dict)