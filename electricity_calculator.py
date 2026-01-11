name=input("Enter name:")
age=int(input("Enter Age:"))
mobile=input("Enter mo.")
unit=int(input("enter unit consummed:"))
late_paid=input("Late payment (y/n) ?:").lower()

if unit <=100:
    bill=unit
elif unit <=200:
    bill=100+(unit-100)*10
else:
    bill=100+1000+(unit-200)*20
if late_paid=="y"or "Y":
    bill+=50
    print("<-----Deatil----->")
    print(f"Name of employee :{name}")
    print(f"Age of employee :{age}")
    print(f"Mobile number:{mobile}")
    print(f"Unit consumed :{unit}")
    print(f"Total bill :{bill}")

