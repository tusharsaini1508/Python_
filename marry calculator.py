gender=input("enter your gender (m/f): ")
if gender=="m":
    print("you are male")
  
elif gender=="f":
  print("you are female")

  
age=int(input("Enter your age"))
if age>=18:
  print(f"you are an adult your age =:{age}")

else:
  print(f"you are not an adult your age is {age}")

if gender=="m":
  if age>=21:
    print(f"you can marry now your age is {age}")
  else:(f"you can't marry now your age is {age}")
    

elif gender=="f":
  if age>=18:
    print(f"you can marry now your age is =:{age}")
  else:(f"you can't marry now your age is =:{age}")
    
