#Grading system for the colleges or school their are two choice in this code
# 1 = For find the Grades by input number 
# 2 = For find the Numbers by input grades


choice = int(input("Enter your choice (1 for Grade, 2 for numbers): "))

if choice == 1:
    name = input("Enter your name: ")
    Grade = input("Enter your grade: ")
    if Grade == "O":
        print(f"{name}Your marks are between 90-100")
    elif Grade == "D+":
        print(f"{name}Your marks are between 80-89")
    elif Grade == "D":
        print(f"{name}Your marks are between 75-79")
    elif Grade == "A+":
        print(f"{name}Your marks are between 70-74")
    elif Grade == "A":
        print(f"{name}Your marks are between 60-69")
    elif Grade == "B+":
        print(f"{name}Your marks are between 50-59")
    elif Grade == "B":
        print(f"{name}Your marks are between 40-49")
    elif Grade == "C":
        print(f"{name}Your marks are between 33-39")
    elif Grade == "F":
        print(f"{name}Your marks are between 0-32")
    elif Grade == "AAA":
      print("Your marks are 0-0 may be you are ABSENT")
    else:
        print("Invalid grade")

elif choice == 2:
    name = input("Enter your name: ")
    number = int(input("Enter your number: "))

    if number >= 90 and number <= 100:
        print(f"Hi {name}, your grade is ,O, (Outstanding)")
    elif number >= 80 and number <= 89:
        print(f"Hi {name}, your grade is ,D+, (Excellent)")
    elif number >= 75 and number <= 79:
        print(f"Hi {name}, your grade is ,D, (Distinction)")
    elif number >= 70 and number <= 74:
        print(f"Hi {name}, your grade is ,A+, (Very Good)")
    elif number >= 60 and number <= 69:
        print(f"Hi {name}, your grade is ,A, (Good)")
    elif number >= 50 and number <= 59:
        print(f"Hi {name}, your grade is ,B, (Average)")
    elif number >= 40 and number <= 49:
        print(f"Hi {name}, your grade is ,C, (Satisfactory)")
    elif number >= 0 and number <= 39:
        print(f"Hi {name}, your grade is ,U, (Re-Appear)")
    else:
        print(f"Hi {name}, your grade is ,AAA, (ABSENT)")
    
else:
    print("invalid choice or wrong choice  ")


