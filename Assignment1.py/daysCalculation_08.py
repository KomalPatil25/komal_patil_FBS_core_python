days = int(input("Enter the days: "))

years = days // 365 # Find years

days = days % 365 # How days are remaining

weeks = days // 7 # Find weeks

days = days % 7 # How days are remaining

print(f'{years} years {weeks} weeks {days} days')