
list=[1,2,3,4,5]
length=len(list)
first=list[0]
for i in range(1,length):
    list[i-1]=list[i]
list[length-1]=first

print(list)