def palindrome():
    word=input("enter a word :")
    #words having spaces
    if (" ") in word:
        #remove the space 
        new=word.replace(" ", "")
        backwards=new[::-1]
        #check if the word is palindrome
        if new==backwards:
            print ("this word is a palindrome")
        else:
            print("it's not ")
    #for words without spaces 
    else :
        backwards_1=word[::-1]
        #check if the word is palindrome
        if word==backwards_1:
            print ("this word is a palindrome")
        else:
            print(word,"is not a palindrome")
palindrome()
