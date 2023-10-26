x=float(input("enter the value of first number"))
y=float(input("enter the value of second number"))
calculation=input("enter the choice +,-,*,/")
if calculation=="+":
  print(f"The addition of x and y is = {x+y}")

elif calculation=="-":
  print(f"The Subtraction of x and y is ={x-y} ")

elif calculation=="*":
  print(f"The multiplication of x and y is = {x*y}")

elif calculation=="/":

  if y==0:
    print("division by zero not allowed")
    if x==0:
      print("division by zero is not allowed")
  else:
    print(f"the division of x and y is {x/y}")

