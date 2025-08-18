def fibonacci(num):
 a = 1
 b = 0

 for i in range(1, num + 1):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    
# num = int(input("Enter the number: "))  
# fibonacci(num) 
fibonacci(6) 
