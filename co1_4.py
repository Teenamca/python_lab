lmt=int(input("Enter the limit"))
list1=[]
print("Enter the numbers")
for i in range(lmt):
    n=int(input())
    if(n>100):
        list1.append("over")
    else:
        list1.append(n)
    print(list1)