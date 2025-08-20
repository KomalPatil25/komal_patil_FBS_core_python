def is_palindrome(num, rev = 0, orig = 0):
    if(num == 0):
        return rev
    else:
        return is_palindrome(num // 10, rev * 10 + (num % 10), orig)

num = int(input("Enter the number: "))
res = is_palindrome(num)
if(num == res):
    print(f'{num} is palindrome.')
else:
    print(f'{num} is not palindrome .')

