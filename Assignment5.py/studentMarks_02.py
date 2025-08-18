num_student = int(input("enter the number of students: "))

total_percentage_sum = 0

for student in range(1, num_student + 1):
    total_marks = 0
    print(f"\nEntering marks for student {student}: ")

    for sub in range(1, 6):
        marks = float(input(f"Enter marks for subject {sub}: "))

        total_marks += marks

    percentage = (total_marks / 500) * 100

    print(f"Percentage for student {student}: {percentage}")

    total_percentage_sum += percentage

average_percentage = total_percentage_sum / num_student

print(f'\nAverage percentage of all students: {average_percentage}')



    

