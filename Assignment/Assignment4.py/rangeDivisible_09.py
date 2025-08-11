n1 = int(input("Enter the number: "))

divisor = int(input("Enter the divisor: "))

for num in range(1, n1+1):
    if(num % divisor == 0):
        print(num, end=" ")