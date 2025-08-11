num = int(input("Enter the number: "))
sum = 0
for digits in str(num):
    digit = int(digits)

    fact = 1
    for i in range(1, digit+1):
        fact *= i

    sum += fact

if(sum == num):
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not strong number.")