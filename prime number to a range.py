
number=int(input("Enter your number"))
test_list=[]
print(f"the list is {test_list}")
test_list.extend(range(1,number))
prime=[]
for i in test_list:
  c=0
  for j in range(1,i):
    if i%j==0:
      c+=1
  if c==1:
    prime.append(i)
print(f"the prime numbers are {prime}")