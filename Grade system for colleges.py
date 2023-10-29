choice=int(input("Enter your choice 1 For Grade 2 for numbers"))
if choice==1:
  name=input("Enter your name =:")
  number=int(input("Enter your number =:"))
  if number>=90and number<=100:
    print(f"hii {name} your grade is ,O,= Outstanding")
  elif number>=80and number<=89:
      print(f"hii {name} your grade is ,D+,= Excellent")
  elif number>=75and number<=79:
        print(f"hii {name} your grade is ,D,= Destinction")
  elif number>=70and number<=74:
          print(f"hii {name} your grade is ,A+,= Very Good")
  elif number>=60and number<=69:
            print(f"hii {name} your grade is ,A,= Good")
  elif number>=50and number<=59:
              print(f"hii {name} your grade is ,B,= Average")
  elif number>=40and number<=49:
                print(f"hii {name} your grade is ,C,= Satisfactory")
  elif number>=00and number<=39:
                  print(f"hii {name} your grade is ,U,= Re-Appear")
  elif number>=00and number<=00:
                    print(f"hii {name} your grade is ,AAA,=ABSENT")
else:
  if choice==2:
    Grade=input("Enter your grade")
    if Grade=="O":
      print("Your marks between 90-100")
      if Grade=="D+":
        print("Your marks between 80-89")
        if Grade=="D":
          print("Your marks between 75-79")
          if Grade=="A+":
            print("Your marks between 70-74")
            if Grade== "A":
              print("Your marks between 60-69")
              if Grade=="B":
                print("Your marks between 50-59")
                if Grade=="C":
                  print("Your marks between 40-49")
                  if Grade=="U":
                    print("Your marks between 0-39")
                    if Grade=="AAA":
                      print("Your marks between 0-0")
        
      
  
   




