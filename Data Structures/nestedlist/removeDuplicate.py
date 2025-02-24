list2 = list(map(int,input("Enter the numbers seperated with spaces :").split()))
newlist=[]
for i in list2:
    if i not in newlist:
        newlist.append(i)
print(newlist)