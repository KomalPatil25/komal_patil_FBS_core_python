n = int(input("Enter the value of N: "))

series_sum = 0
fact = 1

for i in range(1, n + 1):
    fact *= i
    series_sum += i / fact 

print(f'Sum of the series upto {n} terms is {series_sum}')
