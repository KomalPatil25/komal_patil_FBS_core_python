feet = int(input("Enter the distance in feet: "))
inches = int(input("enter the distance in inches: "))

meters = (feet * 0.3048) + (inches * 0.0254)
whole_meter = int(meters)
centimeters = (meters - whole_meter) * 100

print(f'The distance in feet is {feet} and inches is {inches} after converting in meters is {meters} and centimeters is {centimeters}.')