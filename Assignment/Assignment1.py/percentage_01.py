sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: "))
sub5 = int(input("Enter marks of subject 5: "))

gain_marks = sub1 + sub2 + sub3 + sub4 + sub5

percentage = (gain_marks / 500) * 100

print(f'percentage is {percentage}')