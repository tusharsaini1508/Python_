
name = input("Enter your name: ")
print(f"Hello {name}! Welcome to the bill calculator.")

while True:
    phone_number = input("Enter your phone number: ")

    if phone_number.isdigit() and len(phone_number) == 10:
        print(f"We will send you notifications on your number: {phone_number}")
        break  
    else:
        print("Enter a valid 10-digit phone number.")

address = input("Enter your address: ")
print(f"We can also deliver the food to your address: {address}")

while True:
 Bill = float(input("Enter your bill in $: "))
 if type(Bill) == float or int:
   print(f"Your bill is {Bill}$")
   break
 else:
  print("Enter a valid bill")
 
while True:  
 tip = float(input("Enter your tip % (any value you want): "))
 if type(tip) == float or int:
   print(f"Your tip is {tip}%")
   break

 else:
    print("Enter a valid tip")
  


Final_tip = Bill * (tip / 100)
Total_bill = Bill + Final_tip
print(f"Your total bill is: {Total_bill}$")

# Lucky draw for customers
lucky_draw = int(input("Enter the number (1111, 2222, 3333, 4444): "))

split = int(input("Enter how many people want to share the bill: "))
Total_bill_per_person = Total_bill / split
round_Bill = round(Total_bill_per_person, 2)
print(f"Hi {name}, you should pay the bill of {round_Bill}$")

print(f"{name}, thank you for visiting our cafe. See you again!")

