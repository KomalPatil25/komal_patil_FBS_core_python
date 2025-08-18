def palindrome(num):
    original = num
    rev = 0
    while(num > 0):
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return original == rev

num = int(input("enter the number to check palindrome or not: "))
if(palindrome(num)):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")