
a1=[1,2,3,4,5,6,7]
a2=[2,4,5,8,9,10]

n=len(a1)
m=len(a2)
i,j=0,0
inter=[]
while i<n and j<m:
    if a1[i]<a2[j]:
        i+=1

    elif a2[j]<a1[i]:
        j+=1
    else:
        inter.append(a1[i]) 
        i+=1
        j+=1

print(inter)