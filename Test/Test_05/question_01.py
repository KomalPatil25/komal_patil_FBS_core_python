D = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter the amount: "))
print("Amount: ", amount)

for notes in D:
    if(amount >= notes):
        count = amount // notes
        amount = amount % notes
        print(f"{notes} : {count}")