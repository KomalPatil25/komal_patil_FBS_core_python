a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

sqrt = ((b ** 2) - (4 * a * c)) ** 0.5
result1 = (-b + sqrt) / 2 * a

result2 = (-b - sqrt) / 2 * a

print(f'the result 1 is {result1} and result 2 is {result2}')