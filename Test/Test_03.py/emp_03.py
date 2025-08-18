total_emp = 0
emp = int(input("Enter the number of employee: "))


for i in range(1, emp + 1):
    basic_salary = int(input(f'Basic salary of employee {i}: '))

    if(basic_salary < 2000):
        da = (basic_salary * 10) / 100
        ta = (basic_salary * 12) / 100
        hra = (basic_salary * 15) / 100
    else:
        da = (basic_salary * 15) / 100
        ta = (basic_salary * 18) / 100
        hra = (basic_salary * 20) / 100

    total_salary = basic_salary + da + ta + hra

    print(f'Employee {i} -> Total salary: {total_salary}')

    total_emp += total_salary

print(f'Total salary of all employe is: {total_emp}')