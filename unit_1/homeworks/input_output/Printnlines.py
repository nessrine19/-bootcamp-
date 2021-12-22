file=open("student_names.txt","r")
lines_1=[0,1,2,3,4]
for index,line in enumerate(file):
    if (index in lines_1):
        print(line)
file=open("student_names.txt","r")
lines_1=[5,6,7,8,9]
for index,line in enumerate(file):
    if (index in lines_1):
        print(line)
file.close()
