num_passenger = int(input("Enter number of passenger: "))
ticket_cost = float(input("Enter cost per ticket: "))

total_amount = 0

for i in range(num_passenger):
    age = int(input(f"Enter the age of passenger {i + 1}: "))

    if(age < 12):
        amount = ticket_cost * 0.70 # 30% discount
    elif(age> 59):
        amount = ticket_cost * 0.50 # 50% discount
    else:
        amount = ticket_cost # No discount

    total_amount += amount

print(f"\nTotal ticket amount for all passenger: {total_amount}")