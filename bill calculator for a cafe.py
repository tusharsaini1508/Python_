name=input("Enter your name:= ")
print(f"hii {name} Welcome in bill calculator")

phone_number=input("Enter your phone number")
print(f"we will send you notification on your number =: {phone_number}")

address=input("Enter your address")
print(f"we can also deliver the food on your address =: {address}")

Bill=int(input("Enter your bill in $"))
print(f"Your bill is {Bill}$")

tip=int(input("Enter your tip % anything you want"))
print(f"your tip is {tip}%")

Final_tip=Bill*(tip/100)
Total_bill=Bill+Final_tip
print(f"Your total bill is {Total_bill}$")

split=int(input("Enter how many person want to share the bill"))
Total_bill_per_person=Total_bill/split
round_Bill=round(Total_bill_per_person,2)
print(f"hii {name} you should pay the bill of {round_Bill}$")

print(f"{name} Thank you for visiting our cafe see you again")
