x=float(input("Enter the value of first number"))
y=float(input("Enter the value of second number"))
calculation=input("Enter the choice +,-,*,/")
if calculation=="+":
  print(f"The Addition of {x} and {y} is = {x+y}")

elif calculation=="-":
  print(f"The Subtraction of {x} and {y} is ={x-y} ")

elif calculation=="*":
  print(f"The Multiplication of {x} and {y} is = {x*y}")

elif calculation=="/":

  if y==0:
    print("Division by zero not allowed")
    if x==0:
      print("Division by zero is not allowed")
  else:
    print(f"the Division of {x} and {y} is {x/y}")

