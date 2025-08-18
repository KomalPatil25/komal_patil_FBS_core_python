def sumDigit(num):
    total = 0
    while(num > 0):
        digit = num % 10
        total += digit
        num //= 10
    return total

num = int(input("Enter the number: "))
result = sumDigit(num)
print(f"The sum of digit of {num} is : {result}")