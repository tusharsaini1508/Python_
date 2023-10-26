x=float(input("enter teh value of first number"))
y=float(input("enter the value of second number"))
calculation=input("enter the choice +,-,*,/")
if calculation=="+":
  print(x+y)

elif calculation=="-":
  print(x-y)

elif calculation=="*":
  print(x*y)

elif calculation=="/":
  print(x/y)

if y==0:
  print("division by zero not allowed")
else:
  print(x/y)
