def fibonacci(n, a , b):
    if(n <= 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
num = int(input("Enter the number: "))
result = fibonacci(num, -1, 1)
print(result)
