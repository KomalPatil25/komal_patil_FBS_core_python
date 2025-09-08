n = int(input("Enter the number of elements: "))

numbers = []
for i in range(n):
    num = int(input('Enter the number: '))
    numbers.append(num)

even = []
odd = []

for num in numbers:
    if(num % 2 == 0):
        even.append(num)
    else:
        odd.append(num)

print(f'The even number list is: {even}')
print(f'The odd number list is: {odd}.')