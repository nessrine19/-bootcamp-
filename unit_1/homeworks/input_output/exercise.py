#Read all of the content of the file in one variable.
file=open("student_names.txt","r")
studemts=file.read()
print(studemts)
#Write a list of random names to your file.
names=["ness","james","imene","bob","aymen"]
file=open("student_names.txt","a")
for name in names :
    file.write(name +"\n")
file=open("student_names.txt","r")
studemts=file.read()
print(studemts)
file.close()
#checking if a name is in a file
if "Lara craft"in studemts :
    print("name exists ")
else:
    print("does not exist ")
