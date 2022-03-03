myinput=input("Message: ")
mylist=list(myinput)
for i in range(len(mylist)):
    mylist[i]=chr(ord(mylist[i])+1)
print(i+1)