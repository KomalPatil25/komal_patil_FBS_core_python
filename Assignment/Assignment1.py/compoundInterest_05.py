P = int(input("Enter the P: "))
R = int(input("Enter the R: "))
T = int(input("Enter the T: "))

compound_interest = [P*(1 + R)**T / 100 - P ]
print(compound_interest)