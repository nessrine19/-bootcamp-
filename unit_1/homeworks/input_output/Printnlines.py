with open ("student_names.txt") as file :
    student=file.read()
    print(student)
    list_names=student.splitlines()
print(list_names)
n=int(input("enter n :"))
print(list_names[n:])
print(list_names[:-n])
