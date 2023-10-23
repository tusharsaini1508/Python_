

list=["1","2","3","4","5","6","7","8","9","10"]
list.insert(0,"100")
print(list)

list.extend(["11","12","13","14","15"])
print(list)


list.remove("3")
list.remove("8")
print(list)

#question number 2............


list=["apple","banana","kiwi","orange","grape"]
print(list)
list.sort()
print(list)
list.reverse()
print(list)



# question number 3.................



list=[1,2,3,2,4,2,5,6,2]
print(list)
print(list.count(2))
list.remove(2)
print(list)

# #remove the 2 from the list 



# question nimber 7...........



list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2
print(list3)
list4=list3.index(5)
print("The  index value of 5 =",list4)
list3.insert(2,"10")
print(list3)
list3.remove(3)
print(list3)


#question 4.....................


nested_list=[[1,2],[3,4],[5,6],[7,8]]
print(nested_list)
flat_list=sum(nested_list,[])
print(flat_list)

#question number 4 .........................

list=[[1,2],[3,4],[5,6],[7,8]]
print(list)
new_list=list[0]
new_list.extend(list[1])
new_list.extend(list[2])
new_list.extend(list[3])
print(f"your flat list is {new_list}")

# question no 6 ....................
students = [("Alice", 85,"zem"), ("Bob", 92,"hekk"), ("Eva", 78,"arun"), ("David", 95,"kim")]
students.sort(key=lambda p: p[2])   
print(students)



# question number 5.............................


list=[1, 2, 2, 3, 4, 4, 5, 6, 6, 6]
print(list)
new_list=[]
new_list.append(1)
new_list.append(2)
new_list.append(3)
new_list.append(4)
new_list.append(5)
new_list.append(6)
print(f"your new unique list is {new_list}")