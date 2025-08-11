cp = int(input("Enter the cost price: "))
sp = int(input("Enter the selling price: "))

total = cp - sp
if(sp > cp):
    print(f'{total} this is your profit')

else:
    print(f'{total} this is your loss')