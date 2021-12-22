even_num=[]
#a list that contains all the even numbers between 1 and 299
for i in range (1,299):
    if i%2==0:
        even_num.append(i)
print(even_num)
#print the length of the list
n=len(even_num)
print(n)
#all the squared values of the list.
for i in even_num :
    for k in range(0,i):
        if k**2==i:
            print(i)
#In one line check if 57 is in the list using one line of python.
print("true")if (57 in even_num )else print("false")
