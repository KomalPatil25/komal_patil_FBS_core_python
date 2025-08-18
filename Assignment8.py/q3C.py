def powerSum(num):
    total = 0
    for i in range(1, num + 1):
        total = total + (i ** i)
    return total

num = int(input("Enter the number: "))
result = powerSum(num)
print(f"The sum is: {result}")