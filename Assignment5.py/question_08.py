# # a.factorial
# n = int(input("Enter the number: "))
# fact_sum = 0

# for i in range(1, n+1):
#     fact = 1
#     for j in range(1, i+1):
#         fact *= j
#     fact_sum += fact

# print(f"sum of factorial series: {fact_sum}")

# b.Sum of power
n = int(input("Enter the number: "))
power_sum = sum([n ** i for i in range(1, n+1)])
print(f"Sum of power: {power_sum}")

# # c.Geometric series
# n = int(input("Enter the number: "))
# geo_sum = 0
# term = 1

# for i  in range(n):
#     geo_sum += term
#     term *= 2

# print(f"Sum of geometric series is: {geo_sum}")

# # d. sum of series
# a = float(input("Enter value of a: "))
# sum_series = 0

# for i in range(1, 11):
#     sum_series += (a ** i) / i

# print(f"Sum of series S: {sum_series}")

# # e. sum of series
# x = int(input("Enter value of x: "))
# n = int(input("enter number of term: "))

# sum_series = 0
# sign = 1
# denominator = 1

# for i in range(1, n+1):
#     sum_series += sign * (x ** i)/denominator
#     sign *= -1

#     denominator += 2
# print("Sum of series: ", sum_series)