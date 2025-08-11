sub1 = int(input("Enter the 1st subject marks: "))
sub2 = int(input("Enter the 2nd subject marks: "))
sub3 = int(input("Enter the 3rd subject marks: "))
sub4 = int(input("Enter the 4th subject marks: "))
sub5 = int(input("Enter the 5th subject marks: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
cal_avg = total_marks/5

if(cal_avg >= 80):
    grade = "Distinction"
elif(cal_avg >= 70 and cal_avg <= 80):
   grade = "First Class"
elif(cal_avg >= 60 and cal_avg <= 70):
    grade = "Second Class"
elif(cal_avg >= 50 and cal_avg <= 60):
    grade = "Third Class"
elif(cal_avg >= 40 and cal_avg <= 50):
    grade = "Pass Class"
else:
    grade = "Fail"
print(f'The total marks is {total_marks}.\nThe average is {cal_avg}\n and grade is {grade}')