units=int(input("enter the units: "))
total_bill=0

if(units>0):
    if(units>50):
        if(units>150):
            if(units>250):
                total_bill=50*0.5+(150*0.75)+(250*1.20)
                remaining_unit=units-450
                total_bill=(remaining_unit*1.50)+total_bill
            else:
                total_bill=50*0.5+(150*0.75)
                remaining_unit=units-200
                total_bill=(remaining_unit*1.20)+total_bill
        else:
            total_bill=50*0.5
            remaining_unit=units-50
            total_bill=(remaining_unit*0.75)+total_bill
        
    else:
        total_bill=units*0.5
else:
    print("invalid input")
    
charges=total_bill*(20/100)  
total_bill=charges+total_bill
print(total_bill)