num = int(input("Enter the number: "))

print(f'Integer up to {num} that are not divisible by 2 or 3: ')

for i in range(1, num + 1):
    if(i % 2 != 0 and i % 3 != 0):
        print(i, end=" ")

