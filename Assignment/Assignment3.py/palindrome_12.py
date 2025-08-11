a1 = int(input("enter the number: "))
a2 = int(input("enter the number: "))
a3 = int(input("enter the number: "))

ori_num = (a1 * 100) + (a2 * 10) + (a3)
rev_num = (a3 * 100) + (a2 * 10) + (a1)

if(rev_num == ori_num):
    print(f'{ori_num} is palindrome number.')
else:
    print(f'{ori_num} is not palindrome number.')
