def reverseNum(n):
    rev = 0
    while(n > 0):
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev

n = int(input("Enter a number: "))
result = reverseNum(n)
print(f"The reverse number of {n} is: {result}.")