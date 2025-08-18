cp = int(input("Enter the cost price: "))
discount = int(input("Enter the discount percentage: "))

discount_price = (discount * cp) / 100
selling_price = cp - discount_price

print(f'The selling price is {selling_price}.')