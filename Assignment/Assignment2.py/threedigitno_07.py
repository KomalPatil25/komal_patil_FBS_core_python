num = int(input("Enter the three digit :"))

hundered = num // 100
num = num % 100

tens = num // 10

units = num % 10

sum = hundered + tens + units
print(f'sum of three digits is {sum}')

