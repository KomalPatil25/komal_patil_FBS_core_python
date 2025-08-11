n = int(input("Enter the number: "))

a = -1
b = 1

print("Fibonacci series: ",end=" ")

for i in range(n):
    c = a + b
    print(c ,end=" ")
    a = b
    b = c