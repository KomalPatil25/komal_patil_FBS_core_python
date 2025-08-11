salary = int(input("Enter the salary of employee: "))

da_amt = (salary * 10) / 100 # salary * 0.1
ta_amt = (salary * 12) / 100
hra_amt = (salary * 15) / 100

total_salary = salary + da_amt + ta_amt + hra_amt 

print(f'The total salary of employee is:{total_salary}')