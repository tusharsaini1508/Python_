name=input("Enter your name=: ")

gender=input(f"hii {name} enter your gender (m/f): ")
if gender=="m":
    print(f"hii {name} you are male:")
  
elif gender=="f":
  print(f"hii {name} you are female:")

  
age=int(input("Enter your age:"))
if age>=18:
  print(f"you are an adult your age =:{age}")

else:
  print(f"you are not an adult your age is {age}:")

if gender=="m":
  
  if age>=21:
    print(f"you can marry now your age is=: {age}:")
    
  if age<=21:
    print(f"you can't marry you age =: {age}:")
    

elif gender=="f":
  if age>=18:
    print(f"you can marry now your age is=: {age}:")

  if age<=18:
    print(f"you can't marry you age =: {age}:")
 
  
  
  
  
  
    
