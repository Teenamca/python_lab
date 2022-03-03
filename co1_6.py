lst1 = []
lst2 = []

lst1 = [(item) for item in input("Enter the list1 items seperated by space: ").split()]

lst2 = [item for item in input("Enter the list2 items seperated by space: ").split()]

sum1=str(0)
sum2=str(0)
if len(lst1)==len(lst2) :
    print(" Both list are of equal length")
else:
    print("Two list have unequal length")
for x in lst1:
    sum1=sum1+x
for x in lst2:
    sum2=sum2+x
if sum1==sum2:
    a="equal"
else:
    a="not equal"
print("Sum of two list are",a)
for x in lst1:
    for y in lst2:
        if x==y:
            print(y,"Occurs in both list")