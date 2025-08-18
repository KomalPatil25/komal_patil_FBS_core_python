p1 = int(input("Enter the price: "))
p2 = int(input("Enter the price: "))
p3 = int(input("Enter the price: "))
p4 = int(input("Enter the price: "))
p5 = int(input("Enter the price: "))

total = p1 + p2 + p3 + p4 + p5

gst = total * 18 / 100

total_bill = total + gst

print(f"Total bill is {total}. After adding gst is {total_bill}. \n The amount of gst included in the total bill is {gst}")
