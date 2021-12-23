def prime():
    num= int (input ("add a number :"))
    for i in range (2,num):
        # If num is divisible by any number between 2 and num
        if (num%i)==0:
            print(num,"is not prime")
        break
    else:
        print(num,"is prime")
prime()
