age1 = int(input("Enter the of 1st person age: "))
age2 = int(input("Enter the of 2nd person age: "))
age3 = int(input("Enter the of 3rd person age: "))
age4 = int(input("Enter the of 4th person age: "))
age5 = int(input("Enter the of 5th person age: "))

ticket_amt = int(input("Enter the amount of ticket: "))

# For 1st person 
if(age1 <= 12):
    dis_amt = ticket_amt * 0.3
    amt1 = ticket_amt - dis_amt
elif(age1 >= 59):
    dis_amt = ticket_amt * 0.5
    amt1 = ticket_amt - dis_amt
else:
    amt1 = ticket_amt
print(f'The money need to pay for 1st person {amt1}')

# Foe 2nd person
if(age2 <= 12):
    dis_amt = ticket_amt * 0.3
    amt2 = ticket_amt - dis_amt
elif(age2 >= 59):
    dis_amt = ticket_amt * 0.5
    amt2 = ticket_amt - dis_amt
else:
    amt2 = ticket_amt
print(f'The money need to pay for 2nd person {amt2}')

if(age3 <= 12):
    dis_amt = ticket_amt * 0.3
    amt3 = ticket_amt - dis_amt
elif(age3 >= 59):
    dis_amt = ticket_amt * 0.5
    amt3 = ticket_amt - dis_amt
else:
    amt3 = ticket_amt
print(f'The money need to pay for 3rdt person {amt3}')

# Foe 4th person
if(age4 <= 12):
    dis_amt = ticket_amt * 0.3
    amt4 = ticket_amt - dis_amt
elif(age4 >= 59):
    dis_amt = ticket_amt * 0.5
    amt4 = ticket_amt - dis_amt
else:
    amt4 = ticket_amt
print(f'The money need to pay for 4th person {amt4}')

# Foe 5th person
if(age5 <= 12):
    dis_amt = ticket_amt * 0.3
    amt5 = ticket_amt - dis_amt
elif(age5 >= 59):
    dis_amt = ticket_amt * 0.5
    amt5 = ticket_amt - dis_amt
else:
    amt5 = ticket_amt
print(f'The money need to pay for 5th person {amt5}')

total_amt = amt1 + amt2 + amt3 + amt4 + amt5

print(f'Total amount for all 5 tickets: {total_amt:.2f}')