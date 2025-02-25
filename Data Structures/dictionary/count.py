word = input("Enter the word ")
countD={}
for i in word :
    if i in countD:
        countD[i] += 1
    else :
        countD[i] = 1
print(countD)
        
