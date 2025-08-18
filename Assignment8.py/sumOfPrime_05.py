def sumOfPrime(num):
    total = 0
    for num in range(2, num + 1):
        count = 0
        for i in range(1, num + 1):
            if(num % i == 0):
                 count += 1
        if(count == 2):
            total += num
    return total

num = int(input("Enter the number: "))
res = sumOfPrime(num)
print(f"The sum of prime numbers from 1 to {num} is: {res}")