amount = int(input("Enter the amount: "))

notes = [2000, 500, 200,100, 50, 20, 10, 5, 2, 1]

print("\nMinimum notes needed: ")

total_notes = 0

for note in notes:
    if(amount >= note):
        count = amount // note
        amount = amount % note
 
        total_notes += count
        print(f"{note} : {count}")

print(f"\nTotal number of notes: {total_notes}.")