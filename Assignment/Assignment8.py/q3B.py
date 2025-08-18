def factSum(num):

    fact_sum = 0
    fact = 1
    for i in range(1, num + 1):
        fact *= i
        fact_sum += fact
    return fact_sum

num = int(input("Enter the number: "))
result = factSum(num)
print(f"The sum {num} is: {result}")

