amount = int(input("Enter the amount: "))
temp = amount

two_thousand = temp // 2000
temp = temp % 2000

five_hundered = temp // 500
temp = temp % 500

two_hundered = temp // 200
temp = temp % 200

hundered = temp // 100
temp = temp % 100

fifty = temp // 50
temp = temp % 50

twenty = temp // 20
temp = temp % 20

ten = temp // 10
temp = temp % 10

five = temp // 5
temp = temp % 5

total_notes = two_thousand + five_hundered + two_hundered + hundered + fifty + twenty + ten + five

print(f'''The 2 thousand notes is {two_thousand}. The 5 hundered notes is {five_hundered}. The 2 hundred notes is {two_hundered}. 
The 1 hundered notes is {hundered}. The 50 rupees notes is {fifty}. The 20 rupees notes is {twenty}. 
The 10 rupees notes is {ten}.The 5 rupees notes is {five}.''')
print(total_notes)