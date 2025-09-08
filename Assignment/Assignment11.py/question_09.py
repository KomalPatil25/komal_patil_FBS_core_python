num = int(input("Enter the number: "))

number = list(range(1, num + 1))


square = list(map(lambda x : x ** 2, number))
cube = list(map(lambda x: x ** 3, number))

print(number)
print(square)
print(cube)

