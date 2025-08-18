def sum(num):
    sum = 0

    for i in range(1, num + 1):
        sum += i

    return sum

num = int(input("Enter the number: "))
result = sum(num)
print(f"The sum {num} is: {result}")