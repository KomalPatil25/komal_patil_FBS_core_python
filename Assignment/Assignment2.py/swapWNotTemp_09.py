# Swapping without using temp
a = int(input("Enter the a: "))
b = int(input("Enter the b: "))

#add and store in a
a = a + b

b = a - b
a = a - b

print(f'After swapping a:{a} b:{b}')

# Swapping using trick
a = int(input("Enter the a: "))
b = int(input("Enter the b: "))

a,b = b,a

print(f'After swapping a:{a} b:{b}')