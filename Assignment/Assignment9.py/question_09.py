def power(m, n):
    if(n == 0):
        return 1
    else:
        return m * power(m, n - 1)
    
m = int(input("Enter the number: "))
n = int(input('Enter the number: '))
print(power(m, n))