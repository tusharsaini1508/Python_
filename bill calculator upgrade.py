choice=int(input("Enter your choice 1 for bill 2 for feedback:= "))
if choice==1:
    name=input("Enter your name:= ")
    print(f"hii {name} Welcome in bill calculator")

    phone_number=int(input("Enter your phone number"))
    print(f"we will send you notification on your number =: {phone_number}")

    address=input("Enter your address := ")
    print(f"we can also deliver the food on your address =: {address}")

    Bill=int(input("Enter your bill in $"))
    print(f"Your bill is {Bill}$")

    tip=int(input("Enter your tip % anything you want"))
    print(f"your tip is {tip}%")

    Final_tip=Bill*(tip/100)
    Total_bill=Bill+Final_tip
    print(f"Your total bill is :=  {Total_bill}$")

    #lucky draw for customers

    lucky_draw=int(input("Enter the number from 1111,2222,3333,4444 :=  "))
    if lucky_draw==1111:
      print(f"Congratulations you won a vocher of{Total_bill*13/100}$")
    elif lucky_draw==2222:
      print(f"Congratulations you won a vocher of {Total_bill*19/100}$ ")

    elif lucky_draw==3333:
      print(f"Congratulations you won a vocher of {Total_bill*17/100}")

    elif lucky_draw==4444:
      print(f"Congratulations you won a vocher of {Total_bill*15/100}")

    else:
      print("Sorry you didn't win")

    split=int(input("Enter how many person want to share the bill := "))
    Total_bill_per_person=Total_bill/split
    round_Bill=round(Total_bill_per_person,2)
    print(f"hii {name} you should pay the bill of {round_Bill}$")

    print(f"{name} Thank you for visiting our cafe see you again")


elif choice==2:


    feedback=input("Enter your feedback")
    print(f"Thank you for your feedback {feedback}")

else:
    print("Invalid choice")