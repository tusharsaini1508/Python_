# from turtle import Turtle, Screen
# import random
# brush = Turtle()

# my_Dict={"120","90","60"}
# for_dict={"100","100","100"}

# i=1
# while i<=14:
#     brush.forward(for_dict.random())
#     brush.rt(my_Dict.random())
#     i+=1

# myScreen = Screen()
# myScreen.exitonclick()




from turtle import Turtle, Screen
import random
brush = Turtle()
brush.pensize(40)
colours=["medium blue","deep sky blue","aquamarine","spring green","green yellow","gold","orange","deep pink","dark magenta","dark slate blue","red"]
direction=[90,180,270,360]


i=1
while i<=400:
    brush.pensize(7)
    brush.forward(20)
    brush.color(random.choice(colours))
    brush.setheading(random.choice(direction))


#---------------------------------------------------------------------
# i=1
# while i<=400:
#     brush.color(random.choice(colours) )
#     brush.forward(10)
#     brush.right(90)
#     brush.forward(10)
#     brush.left(90)
#     brush.forward(10)
#     brush.backward(10)
#     brush.left(10)
#     brush.forward(10)
#     brush.left(10)
#     brush.forward(10)
    
        
       

#----------------------------------------------------------------
# brush.penup()
# brush.goto(-90, 0)
# brush.pendown()

# for _ in range(1):
#  brush.color(random.choice(colours))    
#  brush.left(60)
#  brush.forward(100)
#  brush.right(120)
#  brush.forward(100)
#  brush.backward(50)
#  brush.right(120)
#  brush.forward(50)


# #t
# for _ in range(1):
#  brush.color(random.choice(colours)) 
#  brush.penup()
#  brush.goto(50, 0)
#  brush.pendown()

#  brush.right(90)
#  brush.forward(120)
#  brush.backward(0)
#  brush.left(90)
#  brush.forward(70)
#  brush.backward(140)

# #L
# for _ in range(1):
#  brush.color(random.choice(colours))    
#  brush.penup()
#  brush.goto(140, 0)
#  brush.pendown()

#  brush.right(90)
#  brush.forward(90)
#  brush.backward(90)
#  brush.left(90)
#  brush.backward(40)





    
    
#----------------------------------------------------------------   
    
# color={"red","green","blue"}
# brush.pencolor(random.choice(list(color)))

# my_Dict = {120, 90, 60}
# for_dict = {100}

# i = 1
# while i <= 14:
#     brush.forward(random.choice(list(for_dict)))
#     brush.rt(random.choice(list(my_Dict)))
#     i += 1

# brush.circle(-100,180)
# brush.right(90)
# brush.teleport(100,100)
# brush.forward(200)



myScreen = Screen()
myScreen.exitonclick()
