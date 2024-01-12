import turtle as tur        
import colorsys as cs   
name=input("Enter your name :=")      
choice=int(input('Enter your choice for play the rangoli 1 for play 2 for print ypur name :='))

if choice==1:
    
 tur.setup(800, 800)
 tur.speed(0)
 tur.tracer(10)
 tur.width(2)                
 tur.bgcolor("black")

 for j in range(30):          
    for i in range(15):      
        tur.color(cs.hsv_to_rgb(i /15, 1, 1))
        
        tur.right(90)
        tur.circle(200 - j * 4, 90)
        tur.left(90)
        tur.circle(200 - j * 4, 90)
        tur.right(180)
        tur.circle(50, 24)
 tur.hideturtle()          
 tur.done() 
else :
    
    print(f"hii {name } if you want to see the rangoli run this code again and select the 1 in choice")